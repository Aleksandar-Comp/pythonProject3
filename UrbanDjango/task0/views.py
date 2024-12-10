from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    # Получаем все посты
    posts = Post.objects.all().order_by('-created_at')

    # Получаем количество постов на странице из GET-параметров, если оно указано
    per_page = request.GET.get('per_page', 5)  # по умолчанию 5 постов на странице
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 5  # если не число, то ставим значение по умолчанию

    # Настроим пагинацию
    paginator = Paginator(posts, per_page)

    # Получаем номер текущей страницы из запроса
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Передаем данные в шаблон
    return render(request, 'second_task/post_list.html', {'page_obj': page_obj, 'per_page': per_page})