from django.shortcuts import render


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, "fourth_task/cart.html")