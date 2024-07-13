from django.shortcuts import render
from .models import Portfolio
from .models import Comment
from django.http import HttpResponse
import json
# port = Portfolio.objects.create(name='HUi', occupation='Killer')
# async def getPort():
#     port = await Portfolio.objects.aget(id=1)
#     print(port.name)
# asyncio.run(getPort())





def getPorts(req):
    ports = Portfolio.objects.all()
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
        obj['photo'] = p.photo
        obj['contacts'] = p.contacts
        obj['age'] = p.age
        obj['ifOnlineWork'] = p.ifOnlineWork
        obj['about'] = p.about
        data.append(obj)
    return HttpResponse(str(json.dumps(data)), content_type='text/plain')
def createPort(req):
    
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
        ifOnlineWork=req.POST.get('ifOnlineWork'),
        about=req.POST.get('about'),
    )
    return render(req, 'portfolios.html')
def getPortById(req):
    ID = req.path.split('/getOnePort__')[1]
    p = Portfolio.objects.get(id=ID)
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
    return HttpResponse(str(json.dumps(obj)), content_type='text/plain')


def editPort(req):
    ID = req.path.split('/editPort__')[1]
    p = Portfolio.objects.get(id=ID)
    p.name=req.POST.get('name')
    p.occupation=req.POST.get('occupation')
    p.salary=req.POST.get('salary')
    p.exp=req.POST.get('exp')
    p.education=req.POST.get('education')
    p.skills=req.POST.get('skills')
    p.citizenship=req.POST.get('citizenship')
    p.location=req.POST.get('location')
    p.photo=req.POST.get('photo')
    p.contacts=req.POST.get('contacts')
    p.age=req.POST.get('age')
    p.ifOnlineWork=req.POST.get('ifOnlineWork')
    p.about=req.POST.get('about')
    p.save()
    return render(req, 'portfolios.html')

'''-----------------------Pages-------------------------'''

def homepage(request):
    return render(request, 'indexx.html')

def portfolios(req):
    return render(req, 'portfolios.html')

def creation(req):
    return render(req, 'createPort.html')

def find(req):
    return render(req, 'find.html')

'''-----------------------------------------------------'''

def deleteAll(req):
    print('here')
    Portfolio.objects.all().delete()
    return HttpResponse('ok')
def deleteOne(req):
    Portfolio.objects.get(id=req.path.split('/deleteOne_')[1]).delete()
    return HttpResponse('ok')
def search(req):
    return render(req, 'search.html')
def sendComment(req):
    data =  json.loads(req.body)
    print(type(data))
    Comment.objects.create(
        text=data['text'],
        date='01.01.2021',
        ref='none',
        author='anonym',
        verified='verificated',
        idToPort=data['idToPort'],
    )
    obj = {
        'text' : data['text'],
        'date' : '01.01.2021',
        'ref' : 'none',
        'author' : 'anonym',
        'verified' : 'verificated',
        'idToPort' : data['idToPort'],
    }
    return HttpResponse(str(json.dumps(obj)), content_type='text/plain')
def getCommentsByPortId(req):
    ID = req.path.split('__')[1]
    print(ID)
    comments = Comment.objects.filter(idToPort=ID)
    data = []
    for comment in comments:
        obj = {}
        obj['text'] = comment.text
        obj['date'] = comment.date
        obj['ref'] = comment.ref
        obj['author'] = comment.author
        obj['verified'] = comment.verified
        obj['idToPort'] = comment.idToPort
        print(obj)
        data.append(obj)
    return HttpResponse(str(json.dumps(data)), content_type='text/plain')
