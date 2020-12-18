from django.contrib.admin import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ExampleModel, Partner, Faq, Article


@register(User)
class UserAdmin(BaseUserAdmin):
    pass


@register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'website', 'logo', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('question', 'answer')
    list_editable = ('is_published',)


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'description', 'is_published', 'created')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title', )}
