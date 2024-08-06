from django.shortcuts import render
from .models import Portfolio
from .models import Comment
from .models import User
from django.http import HttpResponse
import json
from pathlib import Path

def ifEmail(req):
    try:
        user = User.objects.get(email=req.path.split('/isThisEmailRegistered__')[1])
    except:
        return HttpResponse('no', content_type='text/plain')
    else:
        return HttpResponse('yes', content_type='text/plain')
    
def ifUser(req):
    try:
        userName = User.objects.get(userName=req.path.split('/isThisUserRegistered__')[1])
    except:
        return HttpResponse('no', content_type='text/plain')
    else:
        return HttpResponse('yes', content_type='text/plain')
def createUser(req):
    data = json.loads(req.body)
    try:
        User.objects.create(
            userName=data['userName'],
            password=data['password'],
            email=data['email'],
        )
    except:
        return HttpResponse('not ok', content_type='text/plain')
    else:
        return HttpResponse('ok', content_type='text/plain')
def check(req):
    data = json.loads(req.body)
    user = User.objects.get(userName=data['userName'])
    if user.password == data['password']:
        return HttpResponse('yes', content_type='text/plain')
    else:
        return HttpResponse('no', content_type='text/plain')
