from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo


# Create your views here.
def index(request):
    todo_list = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'title': 'Index', 'todo_list': todo_list})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
