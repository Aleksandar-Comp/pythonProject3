from django.shortcuts import render
# from django.core.paginator import Paginator
# from .models import Post
#
#
# def post_list(request):
#     # получаем все посты
#     posts = Post.objects.all()
#
#     # создаем пагинатор
#     paginator = Paginator(posts, 3)  # 10 постов на странице
#
#     # получаем номер страницы, на которую переходит пользователь
#     page_number = request.GET.get('page')
#
#     # получаем посты для текущей страницы
#     page_posts = paginator.get_page(page_number)
#     context = {
#         'posts': posts,
#         'paginator': paginator,
#         'page_number': page_number,
#         'page_posts': page_posts
#     }
#     # передаем контекст в шаблон
#     return render(request, 'index.html', {'page_posts': page_posts})
