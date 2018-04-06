import json

from django.core.exceptions import ObjectDoesNotExist

from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS, csrf_exempt
from tastypie.exceptions import NotFound
from tastypie import http

from news import models as news_models


class NewsResource(ModelResource):

    class Meta:
        allowed_methods = ['get', 'post', 'delete']
        detail_allowed_method = ['get', 'delete']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        fields = ['id', 'title', 'content', 'status', 'topic']
        filtering = {
            'id': ALL,
            'topic': ALL_WITH_RELATIONS,
            'status': ALL
        }
        queryset = news_models.News.objects.filter(status__in=[1,2])
        resource_name = 'news'
    
    def wrap_view(self, view):
        @csrf_exempt
        def wrapper(request, *args, **kwargs):
            request.format = kwargs.pop('format', None)
            wrapped_view = super(NewsResource, self).wrap_view(view)
            return wrapped_view(request, *args, **kwargs)

        return wrapper

    def build_filters(self, filters=None, ignore_bad_filters=False):
        orm_filters = super(NewsResource, self).build_filters(filters)
        if filters is None:
            filters = {}
        if "topic" in filters:
            orm_filters["topic__name"] = filters['topic']

        return orm_filters

    def dehydrate(self, bundle):
        bundle.data['topic'] = list(bundle.obj.topic.all())
        
        return bundle

    def hydrate_m2m(self, bundle):
        for topic in bundle.data['topic']:
            bundle.obj.topic.add(topic)

        return bundle

    def obj_delete(self, bundle, **kwargs):
        obj = self.obj_get(bundle=bundle, **kwargs)
        obj.status = 3
        obj.save()


class NewsDeletedResource(ModelResource):
    
    class Meta:
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        fields = ['id', 'title', 'content', 'status', 'topic']
        filtering = {
            'id': ALL,
            'topic': ALL_WITH_RELATIONS,
            'status': ALL
        }
        queryset = news_models.News.objects.filter(status=3)
        resource_name = 'news-deleted'

    def dehydrate(self, bundle):
        bundle.data['topic'] = list(bundle.obj.topic.all())
        
        return bundle
