from django.shortcuts import render
from .models import Portfolio
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
    return render(req, json.dumps(data), content_type='text/plain')
    
def homepage(request):
    return render(request, 'indexx.html')
def portfolios(req):
    return render(req, 'portfolios.html')
