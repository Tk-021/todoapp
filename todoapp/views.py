from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user = request.user, todo_item=task)
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)
    context = {
            'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        email  = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 4:
            messages.error(request, 'Password is too short')
            return redirect('register')
        
        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Error, Username taken, Try another username')
            return redirect('register')


        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.error(request, 'User Successfully created. Login')
        return redirect('login')
    return render(request, 'todoapp/register.html', {})

# def delete(request, id):
#     try:
#         item = get_object_or_404(todo, id=id)
#     except todo.DoesNotExist:
#         return redirect('home')
#     item.delete()
#     return redirect('home')

def delete(request, task):
    try:
        item = todo.objects.get(id=task)
    except todo.DoesNotExist:
        return render(request, 'todoapp/todo.html', {"error":"Item does not exist"})
    item.delete()
    return redirect('home')

def update(request, task):
    item = todo.objects.get(id=task)
    item.status = True
    item.save()
    return redirect('home')

def notes(request,id):
    item = todo.objects.get(id=id)
    item.status = False
    item.save()
    return redirect('home')

    




    
    

    

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            messages.error(request, 'Error, User does not exist')
            return redirect('login')




    return render(request, 'todoapp/login.html', {})

def logoutpage(request):
    logout(request)
    return redirect('login')