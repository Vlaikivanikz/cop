from django.shortcuts import render
from django import http as http

def homepage(request):
    code = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hellow</h1>
</body>
</html>'''
    return http.HttpResponse()
