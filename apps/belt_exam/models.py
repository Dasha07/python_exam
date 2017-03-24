from __future__ import unicode_literals
from collections import defaultdict, deque
from django.db import models
from django.contrib import messages
from datetime import datetime
import codecs
import random
import bcrypt
import re

class UserManager(models.Manager):
    def register(self, request):
        name = request.POST['reg_name']
        alias = request.POST['reg_alias']
        email = request.POST['email']
        reg_password = request.POST['reg_password']
        reg_password2 = request.POST['reg_password2']
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        valid = True

        if not name:
            messages.warning(request, "Name cannot be blank.")
            valid = False
        if not alias:
            messages.warning(request, "Alias cannot be blank.")
            valid = False
        if not re.match(regex, email):
            messages.warning(request, "Invalid Email.")
            valid = False
        if len(reg_password) < 8:
            messages.warning(request, "Password must be longer than 8 characters.")
            valid = False
        if reg_password != reg_password2:
            messages.warning(request, "Passwords do not match")
            valid = False
        else:
            if valid == True:
                hashedpw = bcrypt.hashpw(reg_password.encode('UTF-8'), bcrypt.gensalt())
                makeuser = User.objects.create(name = name, alias = alias, email = email, password = hashedpw)
                return makeuser
                messages.success(request, "You have successfully registered, please Login.")
            if User.objects.filter(email = email):
                messages.warning(request, "You have registered with this email before, Please login.")
                valid = False


        return False


    def userLogin(self, request):
        email = request.POST['email']
        loginpassword = request.POST['password']
        valid = False

        if len(email) < 1:
            messages.warning(request, "Email cannot be blank!")
            return False
        if len(loginpassword) < 1:
            messages.warning(request, "Password cannot be blank!")
            return False
        try:
            user = User.objects.get(email = email)
        except:
            messages.warning(request, "User does not exist!")
            return False
        if bcrypt.hashpw(loginpassword.encode(), user.password.encode()) == user.password.encode():

            request.session['user_id'] = user.id
            request.session['name'] = user.name
            return True
        else:
            messages.warning(request, "Password is incorrect!")
            return False



class User(models.Model):
      name = models.CharField(max_length=45, default='')
      alias = models.CharField(max_length=45, default='')
      email = models.CharField(max_length=45, default='')
      password = models.CharField(max_length=200, default='')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = UserManager()

class Friend(models.Model):
    friend = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
