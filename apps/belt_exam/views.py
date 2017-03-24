from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserManager, User, Quote, Favorite

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
def new_user(request):
	return render(request, 'belt_exam:new_user')



def home(request):
    users = User.objects.all()
    try:
        User.objects.get(id = request.session['user_id'])
    except:
        return redirect('/')
    new_user = User.objects.get(id = request.session['user_id'])
    user = User.objects.get(id = request.session['user_id'])
    user_id = request.session['user_id']
    context = {
    'user': user,
    'new_user' : User.objects.get(id=request.session['user_id']),
    'all_quotes' : Quote.objects.all().order_by('-created_at'),
    'my_favorite' : Favorite.objects.filter(user_id=user_id).order_by('-created_at')
        }
    return render(request, 'belt_exam/home.html', context)

def add(request, quote_id):
    new_user = User.objects.get(id=request.session['user_id'])
    new_quote = Quote.objects.get(id=quote_id)
    new_favorite =Favorite.objects.create(user=new_user, quote=new_quote)
    return redirect('belt_exam:home')

def drop(request, quote_id):
    user_id = request.session['user_id']
    Favorite.objects.filter(user=user_id, quote=quote_id).delete()
    return redirect('belt_exam:home')

def show_user(request, user_id):
    new_user = User.objects.get(id=user_id)
    my_quotes = Quote.objects.filter(posted_by=user_id)

    context = {
    'user' : new_user,
    'my_quotes': my_quotes
    }
    return render(request, 'belt_exam/users.html', context)

def create(request):
    name = request.POST['name']
    message = request.POST['message']
    user = User.objects.get(id=request.session['user_id'])
    if len(name) < 3:
        messages.add_message(request, messages.ERROR, 'Quoted by should be more than 3 characters')
    if len(message) < 10:
        messages.add_message(request, messages.ERROR, 'Message should be more than 10 characters')
    else:
        Quote.objects.create(name=name, message=message, posted_by=user)
    return redirect('belt_exam:home')


def logout(request):
    request.session.delete()
    return redirect('/')
