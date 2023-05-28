from django.contrib import admin

from news_app import models
from news_app.models import Category, News, Contact, Comment


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title', 'body')}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


@admin.register(Comment)
class ContactAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'post']
    pass