from pathlib import Path
from django.http import HttpResponse

def sendHtml(name):
    HTML = Path(Path(__file__).resolve().parent.parent, 'html_files')
    return HttpResponse(open(Path(HTML, name)).readlines(), content_type='text/html')