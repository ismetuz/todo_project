from django.contrib import admin
from .models import Todo, Category
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'category',
        'title',
        'is_active',
        'created_at',
        'updated_at',

    ]
    list_editable =[
        'is_active',
    ]
    list_display_links = [
        'pk',
        'category',
        'title'
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
    ]
    list_display_links = [
        'slug',
    ]




admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)