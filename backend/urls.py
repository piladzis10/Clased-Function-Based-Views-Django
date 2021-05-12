
from django.urls import path
from .views import todo_list, todo_detail
from .views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView

urlpatterns = [
    path('todo_list', TodoListView.as_view(), name="todo_list"),
    path("add/", TodoCreateView.as_view(), name="todo_create"),
    path('<int:pk>/', TodoDetailView.as_view(), name="todo_detail"),
    path('<int:pk>/update', TodoUpdateView.as_view(), name="todo_update"),
   
]