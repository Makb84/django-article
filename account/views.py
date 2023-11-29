from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Article, Category

from blog.forms import ArticleAddForm

# Create your views here.

@login_required
def home(request):
    # articles = Article.objects.published()
    if request.user.is_superuser:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(author=request.user)
    
    context = {
        # "articles": Article.objects.all()
        # "articles": Article.objects.filter(status='p').order_by('-publish'), # [:2] #bracket shows number of articles that we want to show
        "articles": articles,
        "category": Category.objects.filter(status=True) # [:2] #bracket shows number of articles that we want to show
    }
    return render(request, 'registration/home.html', context)



def article_create(request):

    articleaddform = ArticleAddForm()
    if request.POST:
        articleaddform = ArticleAddForm(request.POST, request.FILES)        
        if articleaddform.is_valid():
            articleaddform.save()

        return redirect('account:home')

    context = {
        'form': articleaddform,
    }

    return render(request, 'registration/article-create-update.html', context)
        