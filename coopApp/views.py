from django.shortcuts import render
from .models import Portfolio
from django.http import HttpResponse
import asyncio
import json
# port = Portfolio.objects.create(name='HUi', occupation='Killer')
# async def getPort():
#     port = await Portfolio.objects.aget(id=1)
#     print(port.name)
# asyncio.run(getPort())
ports = Portfolio.objects.all()


def getPorts(req):
    data = []
    for p in ports:
        obj = {}
        obj['id'] = p.id
        obj['name'] = p.name
        obj['occupation'] = p.occupation
        obj['salary'] = p.salary
        obj['exp'] = p.exp
        obj['education'] = p.education
        obj['skills'] = p.skills
        obj['citizenship'] = p.citizenship
        obj['location'] = p.location
        # obj['photo'] = p.photo
        obj['contacts'] = p.contacts
        obj['age'] = p.age
        obj['ifOnlineWork'] = p.ifOnlineWork
        obj['about'] = p.about
        data.append(obj)
    return HttpResponse(str(json.dumps(data)), content_type='text/plain')
def createPort(req):
    cond = 0
    if req.POST.get('ifOnlineWork') == 'yes':
        cond = True
    else:
        cond = False
    Portfolio.objects.create(
        name=req.POST.get('name'),
        occupation=req.POST.get('occupation'),
        salary=req.POST.get('salary'),
        exp=req.POST.get('exp'),
        education=req.POST.get('education'),
        skills=req.POST.get('skills'),
        citizenship=req.POST.get('citizenship'),
        location=req.POST.get('location'),
        photo=req.POST.get('photo'),
        contacts=req.POST.get('contacts'),
        age=req.POST.get('age'),
        ifOnlineWork=cond,
        about=req.POST.get('about'),
    )
    return render(req, 'portfolios.html')
    
def homepage(request):
    return render(request, 'indexx.html')
def portfolios(req):
    return render(req, 'portfolios.html')
def creation(req):
    return render(req, 'createPort.html')
