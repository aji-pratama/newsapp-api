import json

from django.core.exceptions import ObjectDoesNotExist

from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS, csrf_exempt
from tastypie.exceptions import NotFound
from tastypie import http

from news import models as news_models


class TopicResource(ModelResource):

    class Meta:
        allowed_methods = ['get', 'post', 'delete']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        fields = ['id', 'name', 'status']
        filtering = {
            'id': ALL,
            'status': ALL
        }
        queryset = news_models.Topic.objects.filter(status__in=[1,2])
        resource_name = 'topic'

    def wrap_view(self, view):
        @csrf_exempt
        def wrapper(request, *args, **kwargs):
            request.format = kwargs.pop('format', None)
            wrapped_view = super(TopicResource, self).wrap_view(view)
            return wrapped_view(request, *args, **kwargs)

        return wrapper

    def dehydrate(self, bundle):
        bundle.data['news'] = list(bundle.obj.news_set.all())

        return bundle

    def obj_delete(self, bundle, **kwargs):
        obj = self.obj_get(bundle=bundle, **kwargs)
        obj.status = 3
        for news in news_models.News.objects.filter(topic=obj):
            news.topic.remove(obj)
        obj.save()


class TopicDeletedResource(ModelResource):
    
    class Meta:
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        fields = ['id', 'name', 'status']
        filtering = {
            'id': ALL,
            'status': ALL
        }
        queryset = news_models.Topic.objects.filter(status=3)
        resource_name = 'topic-deleted'

    def dehydrate(self, bundle):
        bundle.data['news'] = list(bundle.obj.news_set.all())

        return bundle
