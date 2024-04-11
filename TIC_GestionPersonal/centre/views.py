from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def hello_world(request):
    return HttpResponse('Hello World')

def about(request):
    return HttpResponse("<h1>About</h1>")

def index(request):
    professor = {"nom": "John", "cognom": "Doe", "edat": 25}
    template = loader.get_template('index.html')
    dades = template.render({'name':professor["nom"], 'surname':professor["cognom"]})
    return HttpResponse(dades)