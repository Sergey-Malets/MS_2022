from django.shortcuts import render
from .models import Comment, Category, Post


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    # на линии 5 внутри функции view, вы получаете QuerySet , содержащий все сообщения в базе данных.
    # order_by() упорядочивает Queryset в соответствии с приведенным аргументом.
    # Знак минус говорит Django начинать с наибольшего значения, а не с самого маленького.
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.object.filter(
        categories__name__contains=category
    ).order_by('-created_on')
    # Аргумент фильтра сообщает Django, какие условия должны быть выполнены для извлечения объекта.
    # В этом случае нам нужны только сообщения, категории которых содержат категорию,
    # имя которой соответствует названию, указанному в аргументе функции просмотра.
    # Опять же, вы используете order_by()для заказа сообщений, начиная с самых последних.
    # Затем мы добавляем эти сообщения и категорию в context словарь и отображаем наш шаблон.
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(requst, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(requst, "blog_detail.html", context)
