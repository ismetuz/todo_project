from django.contrib import admin
from .models import Todo, Category
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        'created_at',
        'updated_at'
    ]
    list_editable =[
        'is_active'
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
    ]




admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)