from django.urls import path, include
from tastypie.api import Api

from news import api_news, api_topic

v1_api = Api(api_name='api')
v1_api.register(api_news.NewsResource())
v1_api.register(api_news.NewsDeletedResource())
v1_api.register(api_topic.TopicResource())
v1_api.register(api_topic.TopicDeletedResource())

urlpatterns = [
    path('', include(v1_api.urls)),
]
