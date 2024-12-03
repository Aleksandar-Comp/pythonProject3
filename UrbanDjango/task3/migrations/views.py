from django.shortcuts import render




def platform(request):
    title = "Главная страница"
    main = "Главная"
    shop = "Магазин"
    basket = "Корзина"
    context = {
        "title": title, "main": main, "shop": shop, "basket": basket,
    }
    return render(request, 'third_task/platform.html', context)


def games(request):
    return render(request, "third_task/games.html")


def cart(req):
    return render(req, "third_task/cart.html")