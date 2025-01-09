from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home(request):
    articles = Article.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)

def author_list(request):
    authors = Author.objects.all()
    ctx = {'authors': authors}
    return render(request, 'articles/author_list.html', ctx)

def author_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        bod = request.POST.get('bod')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        if first_name and last_name and description and bod and email and image:
            Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                description=description,
                bod=bod,
                email=email,
                image=image
            )
            return redirect('articles:author_list')
    return render(request, 'articles/create-author.html')


def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        bod = request.POST.get('bod')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        if first_name and last_name and description and bod and email and image:
            author.first_name=first_name
            author.last_name=last_name
            author.description=description
            author.bod=bod
            author.email=email
            author.image=image
            author.save()
            return redirect('articles:author_list')
    ctx = {'author': author}
    return render(request, 'articles/create-author.html', ctx)

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk,)
    if request.method == 'POST':
        author.delete()
        return redirect('articles:author_list')
    ctx = {'author': author}
    return render(request, 'articles/confirm-delete.html', ctx)

def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = request.POST.get('author')
        image = request.FILES.get('image')
        if title and content and author_id and image:
            author = Author.objects.get(id=author_id)
            Article.objects.create(
                title=title,
                content=content,
                author=author,
                image=image,
            )
            return redirect('home')
    authors = Author.objects.all()
    ctx = {'authors': authors}
    return render(request, 'articles/create-article.html', ctx)

def blog_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    ctx = {'article': article}
    return render(request, 'articles:confirm-delete.html', ctx)

def blog_detail(request, year, month, day, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    comments = Comment.objects.filter(article=article)
    ctx = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/blog-detail.html', ctx)


def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        if name and email and comment:
            Comment.objects.create(
                article=article,
                name=name,
                email=email,
                comment=comment,
            )
            return redirect('articles:success_commented', pk=article.pk)
    comments = Comment.objects.filter(article=article)
    ctx = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/blog-detail.html', ctx)

def success_commented(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/success-commented.html', {'article': article})