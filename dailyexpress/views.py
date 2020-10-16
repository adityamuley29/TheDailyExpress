from django.shortcuts import render, redirect
import requests
import json
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

@login_required(login_url='login')
def home(request):
    news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&apiKey=9144bd1952654f95a5597b25a44e8e59")
    api = json.loads(news_api.content)
    return render(request, 'home.html', {'api': api})


@login_required(login_url='login')
def bnews(request):
    b_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9144bd1952654f95a5597b25a44e8e59")
    b_api = json.loads(b_news_api.content)

    return render(request, 'bnews.html', {'b_api': b_api})


@login_required(login_url='login')
def enews(request):
    e_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9144bd1952654f95a5597b25a44e8e59")
    e_api = json.loads(e_news_api.content)

    return render(request, 'enews.html', {'e_api': e_api})


@login_required(login_url='login')
def hnews(request):
    h_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9144bd1952654f95a5597b25a44e8e59")
    h_api = json.loads(h_news_api.content)

    return render(request, 'hnews.html', {'h_api': h_api})


@login_required(login_url='login')
def scnews(request):
    sc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9144bd1952654f95a5597b25a44e8e59")
    sc_api = json.loads(sc_news_api.content)

    return render(request, 'scnews.html', {'sc_api': sc_api})


@login_required(login_url='login')
def snews(request):
    s_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9144bd1952654f95a5597b25a44e8e59")
    s_api = json.loads(s_news_api.content)

    return render(request, 'snews.html', {'s_api': s_api})


@login_required(login_url='login')
def tnews(request):
    t_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9144bd1952654f95a5597b25a44e8e59")
    t_api = json.loads(t_news_api.content)

    return render(request, 'tnews.html', {'t_api': t_api})
