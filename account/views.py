from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Article, Category

# Create your views here.

@login_required
def home(request):
    articles = Article.objects.published()
    
    context = {
        # "articles": Article.objects.all()
        # "articles": Article.objects.filter(status='p').order_by('-publish'), # [:2] #bracket shows number of articles that we want to show
        "articles": articles,
        "category": Category.objects.filter(status=True) # [:2] #bracket shows number of articles that we want to show
    }
    return render(request, 'registration/home.html', context)

def article(request):

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

    return render(request, "registration/home.html", context)