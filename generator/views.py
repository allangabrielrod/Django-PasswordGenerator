from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    base_characters = 'abcdefghijklmnopqorstuvwxyz'
    special_characters = '!@#$%&*?'
    numbers = '1234567890'

    characters = list(base_characters)

    if request.GET.get('uppercase'):
        characters.extend(list(base_characters.upper()))

    if request.GET.get('special'):
        characters.extend(list(special_characters))

    if request.GET.get('numbers'):
        characters.extend(list(numbers))

    length = int(request.GET.get('length', 12))

    password = ''

    for i in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})
