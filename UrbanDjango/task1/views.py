from django.shortcuts import render
"""from django.http import HttpResponse
from .forms import UserRegister
from .models import *



def menu(request):
    return render(request, 'menu.html')


def home(request):
    return render(request, 'home.html')


def shop(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'shop.html', context)


def basket(request):
    return render(request, 'basket.html')


def sign_up(request):
    users = Buyer.objects.all()
    info = {}
    context = {
        'info': users
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            balance = form.cleaned_data['balance']
            age = form.cleaned_data['age']

            if not Buyer.objects.filter(name=name).exists():
                Buyer.objects.create(name=name, balance=balance, age=age).save()
                return HttpResponse(f'Приветствуем, {name}!')
            else:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})"""

# Create your views here.