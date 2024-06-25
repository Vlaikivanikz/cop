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
        data.append(obj)
    return HttpResponse(str(json.dumps(data)), content_type='text')
    
def homepage(request):
    return render(request, 'indexx.html')
def portfolios(req):
    return render(req, 'portfolios.html')
