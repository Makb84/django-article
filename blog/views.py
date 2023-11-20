from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category


# Create your views here.


# http test-------------------

# def home(request):
#     return HttpResponse("hello world")

# ----------------------------

# these are Json tests --------------------------------------


# def api(request):
#     return JsonResponse({"Title": "سلام دنیا"})

# def api(request):
#     data = {
#         "1": {
#             "title": "مقاله اول",
#             "id": 20,
#             "slug": "first article"
#         },

#         "2": {
#             "title": "مقاله دوم",
#             "id": 21,
#             "slug": "second article"
#         }

#     }
#     return JsonResponse(data)


#------------------------------------------------------------


# def home(request):

#     context = {
#         "articles":[
#             {
#             "username": "Amin",
#             "age": 24,
#             "job": "Programer",
#             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1920px-Google_2015_logo.svg.png"
#             },
#             {
#             "username": "Alireza",
#             "age": 24,
#             "job": "Programer",
#             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1920px-Google_2015_logo.svg.png"
#             },
#         ]
        
#     }

#     return render(request, "blog/home.html", context)






def home(request):

    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 3)  # Show 3 contacts per page.    
    page_number = request.GET.get("page_number")
    print()
    articles = paginator.get_page(page_number)
    for article in articles:
        print(article.title)
    context = {
        # "articles": Article.objects.all()
        # "articles": Article.objects.filter(status='p').order_by('-publish'), # [:2] #bracket shows number of articles that we want to show
        "articles": articles,
        "category": Category.objects.filter(status=True) # [:2] #bracket shows number of articles that we want to show

    }

    return render(request, "blog/home.html", context)

def detail(request, slug):

    context = {
        # "articles": Article.objects.all()
        # "article": Article.objects.get(slug=slug)
        "article": get_object_or_404(Article, slug=slug, status="p"),
        "category": Category.objects.filter(status=True) # [:2] #bracket shows number of articles that we want to show
    }

    return render(request, "blog/detail.html", context)

def category(request, slug):
    
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 3)  # Show 3 contacts per page.    
    page_number = request.GET.get("page_number")
    print()
    articles = paginator.get_page(page_number)
    for article in articles:
        print(article.title)
    context = {
        # "category": get_object_or_404(Category, slug=slug, status="True"),
        "category": category,
        "articles": articles
    }
    return render(request, "blog/category.html", context)

