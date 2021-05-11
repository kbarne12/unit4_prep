from django.shortcuts import render, redirect
# Add the following import

from .models import Todo
from .forms import TodoForm

# Define the home view
def home(request):
  todo = Todo.objects.all()
  return render(request, 'home.html', {'todos':todo})

def add_todo(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      new_todo = form.save(commit=False)
      new_todo.save()
    return redirect('home')
  else:
    form = TodoForm()
    return render(request, 'add.html', {'form':form})

def delete_todo(request, todo_id):
  Todo.objects.get( id = todo_id ).delete()
  return redirect('home')  
