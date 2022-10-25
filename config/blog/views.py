from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from .form import FormComment


def search_view(request):
    # base objects
    posts_pop = Article.objects.all().order_by('-views')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))

    # main
    q = request.POST.get('q')
    posts = Article.objects.filter(is_published=True).filter(content__contains=q)

    context = {
        # base
        'cats': cats,
        'zone_cat': zone_cat,
        # 'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,
        # main
        'posts': posts,
        'q': q,
    }
    return render(request, 'searched.html', context)


def category_view(request, pk):
    # base objects
    posts_pop = Article.objects.all().order_by('-views')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    # main
    cat = Category.objects.get(id=pk)
    posts = Article.objects.filter(cat=cat).filter(is_published=True)

    context = {
        # base
        'cats': cats,
        'zone_cat': zone_cat,
        'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,
        # main
        'posts': posts,
        'cat': cat,
    }
    return render(request, 'category.html', context)


def detail(request, slug):
    form = FormComment(request.POST or None)
    if form.is_valid():
        form.save()
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        comments = Comment.objects.create(name=name, email=email, msg=msg)
    # base objects
    posts_pop = Article.objects.all().order_by('-views')[:3]
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    posts = Article.objects.filter(is_published=True)
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    # main
    obj = posts.get(slug=slug)
    obj.views += 1
    obj.save()
    context = {
        # base
        'cats': cats,
        'zone_cat': zone_cat,
        'posts_car': posts[:3:-1],
        'posts_pop': posts_pop,
        'form': form,
        # main
        'obj': obj,
    }
    return render(request, 'blog-single.html', context)


def home(request):
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    posts = Article.objects.filter(is_published=True)
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    context = {
        'cats': cats,
        'zone_cat': zone_cat,
        'p': p,
        'posts': posts_,
        'posts_car': posts[:3:-1],
    }

    return render(request, 'index.html', context)


def about_view(request):
    cats = Category.objects.all()
    zone_cat = ZoneCat.objects.all()
    posts = Article.objects.filter(is_published=True)
    for cat in cats:
        cat.n = len(Article.objects.filter(cat=cat))
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    context = {
        'cats': cats,
        'zone_cat': zone_cat,
        'p': p,
        'posts': posts_
    }
    return render(request, 'about.html', context)
