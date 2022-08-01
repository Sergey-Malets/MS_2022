from django.shortcuts import render
from .models import Comment, Category, Post
from .forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    # на линии 5 внутри функции view, вы получаете QuerySet , содержащий все сообщения в базе данных.
    # order_by() упорядочивает Queryset в соответствии с приведенным аргументом.
    # Знак минус говорит Django начинать с наибольшего значения, а не с самого маленького.
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    # проверка если метод который пришел с реквеста ПОСТ, т.е. отправляет данные, то создаем экземпляр формы
    # и записываем данные кот. пришли к нам с ПОСТа
    # Затем проверяем валидность формы(все поля заполнены правильно), тогда создаем экземпляр класса коммент,
    # сохраняя в нашу БД
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        'form': form
    }
    return render(request, "blog_detail.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
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
