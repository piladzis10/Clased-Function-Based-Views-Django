from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import Todo

class TodoListView(ListView):
    model = Todo
    queryset = Todo.objects.filter(is_done=False)

class TodoCreateView(CreateView):
    model = Todo
    fields = ['description']

    def get_success_url(self):
        return reverse("todo_list")

class TodoDetailView(DetailView):
    model = Todo

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["is_done"]

    def get_success_url(self):
        return reverse("todo_detail", kwargs={"pk": self.object.pk})
        

def todo_list(request):
    if request.method == 'POST':
        description = request.POST.get("description")

        if description:
            Todo.objects.create(description=description)

            return redirect("todo_list")


    object_list = Todo.objects.filter(is_done=False)

    return render(request, "backend/todo_list.html", {"object_list": object_list})

def todo_detail(request,pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.is_done = True
        todo.save()
        return redirect("todo_list")


    return render(request, "backend/todo_detail.html", {"todo":todo})
