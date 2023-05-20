from django.urls import path
from todo.views import home_view,todo_detail_view

urlpatterns = [
    path('', home_view,name="home" ),
    path('todo/<int:id>',todo_detail_view, name="todo_detail"),
]