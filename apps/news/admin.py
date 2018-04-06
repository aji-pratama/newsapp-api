from django.contrib import admin
from news import models as news_models


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'status']


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


admin.site.register(news_models.News, NewsAdmin)
admin.site.register(news_models.Topic, TopicAdmin)
