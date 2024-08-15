from pathlib import Path
from django.http import HttpResponse
import codecs
from PIL import Image
from .models import Portfolio
from .models import Comment
from .models import User

CSS = Path(Path(__file__).resolve().parent.parent, 'static', 'cop', 'css')
IMG = Path(Path(__file__).resolve().parent.parent, 'static', 'cop', 'img')
def sendHtml(name):
    HTML = Path(Path(__file__).resolve().parent.parent, 'html_files')
    file = codecs.open(Path(HTML, name), "r","utf_8_sig" )
    text = file.read()
    file.close()
    return HttpResponse(text, content_type='text/html')
def getCss(req):
    name = req.path[6:]
    return HttpResponse(open(Path(CSS, name)).readlines(), content_type='text/css')
def getImg(req):
    name = req.path[6:]
    file = open(Path(IMG, name), 'rb')
    return HttpResponse(file, content_type='image/*')