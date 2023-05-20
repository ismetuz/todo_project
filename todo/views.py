from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from todo.models import Todo

    # todos = Todo.objects.filter(
    #     is_active=True,
    #     title__icontains ='todo' #burada title içinde todo olanları da filtreledik
    #     )
    # Hem is_active olacak hemde title içinde todo yazacak
    # eğer bir metnin içinde küçük büyük harf duyarlılığı olmadan bir kelime harf arayacaksak title__icontains='todo' 

def home_view(request):
    todos = Todo.objects.filter(is_active=True)
    context = dict(
        todos=todos
    )
    return render(request, 'todo/todo_list.html', context)


def todo_detail_view(request,id):
    todo = get_object_or_404(Todo, pk=id)
    context = dict(
        todo = todo,
        pk = id,
    )
    return render(request,'todo/todo_detail.html', context)