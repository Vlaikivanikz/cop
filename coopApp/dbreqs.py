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
def getPortByName(req):
    # try:
    Nme = req.path.split('/getPortByName___')[1]
    that = Portfolio.objects.get(userName=Nme)
    data = {}
    data['usr']= reduceBrackets(that.userName)
    data['name']=reduceBrackets(that.name)
    data['occups']=reduceBrackets(that.occupation)
    data['salary']=reduceBrackets(that.salary)
    data['exp']=reduceBrackets(that.exp)
    data['edu']=reduceBrackets(that.education)
    data['skills']=reduceBrackets(that.skills)
    data['age']=reduceBrackets(that.age)
    data['desc']=reduceBrackets(that.about)
    data['lang']=reduceBrackets(that.languages)
    data['hobby'] =reduceBrackets(that.hobby)
    data['phone']=reduceBrackets(that.phone)
    data['mail']=reduceBrackets(that.mail)
    data['location']=reduceBrackets(that.location)
    data['com']=reduceBrackets(that.com)
    data['sch']=reduceBrackets(that.sch)
    return HttpResponse(str(json.dumps(data)), content_type='text/plain')
    # except:
    #     return HttpResponse('not ok', content_type='text/plain')
def save(req):
    data = json.loads(req.body)
    try:
        that = Portfolio.objects.get(userName=data['usr'])
        that.clean()
        print(reduceBrackets(that.occupation))
        that.name=data['name'],
        that.occupation=data['occups'],
        that.salary=data['salary'],
        that.exp=data['exp'],
        that.education=data['edu'],
        that.skills=data['skills'],
        that.age=data['age'],
        that.about=data['desc'],
        that.languages = data['lang'],
        that.hobby = data['hobby'],
        that.phone = data['phone'],
        that.mail = data['mail'],
        that.location = data['location']
        that.sch = data['sch'],
        that.com = data['com']
        that.save()
        print('saved')
    except:
        Portfolio.objects.create(
        userName = data['usr'],
        name=data['name'],
        occupation=data['occups'],
        salary=data['salary'],
        exp=data['exp'],
        education=data['edu'],
        skills=data['skills'],
        age=data['age'],
        about=data['desc'],
        languages = data['lang'],
        hobby = data['hobby'],
        phone = data['phone'],
        mail = data['mail'],
        location = data['location'],
        sch = data['sch'],
        com = data['com']
        )
        print('created')
    print(Portfolio.objects.count())
    return HttpResponse('ok', content_type='text/plain')
def reduceBrackets(str):
    if str == '':
        return str
    elif str[0] == '(' and str[-1] == ')':
        return str[2:-3]
    else:
        return str

# Portfolio.objects.all().delete()

