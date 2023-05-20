from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = 'title')

    def __str__(self):
        return self.title

class Todo(models.Model):
    # category = models.FereignKey(Category, on_delete = models.CASCADE) #bunu kullanmıyoruz çünkü CASCADE yapınca
    #Category silindiğinde tüm ilişkili todolar da silinir..
    
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title