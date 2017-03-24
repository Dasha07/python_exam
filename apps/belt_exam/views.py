from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserManager, User

def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = 0
    return render(request, 'belt_exam/index.html')

def register(request):
    if User.objects.register(request):
        return redirect('belt_exam:home')
    else:
        return redirect('/')

def login(request):
    if User.objects.userLogin(request):
        return redirect('belt_exam:home')
    else:
        return redirect('/')


def home(request):
    users = User.objects.all()
    try:
        User.objects.get(id = request.session['user_id'])
    except:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    context = {
    'users': users,
    'user': user
    }
    return render(request, 'belt_exam/home.html', context)
def add(request, user_id):
    User.objects.create(user_id=user_id)
    return redirect('belt_exam:home')

def logout(request):
    request.session.delete()
    return redirect('/')
