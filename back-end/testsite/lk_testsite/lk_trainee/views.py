from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Главная страница сайта стажёра')

def authorization(request):
    return HttpResponse('<h1>Авторизация</h1>')