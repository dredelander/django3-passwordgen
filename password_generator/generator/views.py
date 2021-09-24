from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home (request):
    return render (request, 'generator/home.html')

def about (request):
    return render (request, 'generator/about.html')

def password (request):

    thepassword = ''

    characters = list('abcdefghjiklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('@#$%&*!~`'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('length'))

    for x in range(lenght):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password': thepassword})