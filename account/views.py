from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldsMixin

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Article, Category

from blog.forms import ArticleAddForm

# Create your views here.

@login_required
def home(request):
    # articles = Article.objects.published()
    # Retrieve articles based on user type (superuser or regular user)    
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


from .decorators import fields_dispatch

@login_required
@fields_dispatch
def article_create(request, fields):
    print(fields)
    # Initialize the form for adding articles    
    articleaddform = ArticleAddForm(fields=fields)

    if request.POST:
    # If the form is submitted, validate the data        
        articleaddform = ArticleAddForm(request.POST, request.FILES)
        if articleaddform.is_valid():
            if request.user.is_superuser:
                # Save the article for superusers
                articleaddform.save()
            else:
                # Save the article with the author for regular users
                obj = articleaddform.save(commit=False)
                obj.author = request.user
                articleaddform.save()
            

        return redirect('account:home')

    context = {
        'form': articleaddform,
        'fields': fields
    }

    return render(request, 'registration/article-create-update.html', context)
        
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden



@login_required
@fields_dispatch
def article_update(request, fields, slug):
    # print(fields)
    # Initialize the form for adding articles
    print(slug)
    article = get_object_or_404(Article, slug=slug)
    # if not request.user.is_superuser and request.user != article.author:
    #     return HttpResponseForbidden("You do not have permission to update this article.")
    
    # if not request.user.is_superuser and request.user == article.author and article.status == 'p':
    #     return HttpResponseForbidden("You do not have permission to update this article.")
    
    if (not request.user.is_superuser) and (request.user != article.author or (request.user == article.author and article.status == 'p')):
        return HttpResponseForbidden("You do not have permission to update this article.")
    
    articleupdateform = ArticleAddForm(instance=article, fields=fields)

    if request.POST:
        # If the form is submitted, validate the data
        articleupdateform = ArticleAddForm(request.POST, request.FILES, instance=article)
        if articleupdateform.is_valid():
            if request.user.is_superuser:
                # Save the updated article for superusers
                articleupdateform.save()
            else:
                # Save the updated article with the author for regular users
                obj = articleupdateform.save(commit=False)
                obj.author = request.user
                articleupdateform.save()

            return redirect('account:home')

    context = {
        'form': articleupdateform,
        'fields': fields,
        'slug': article.slug
    }

    return render(request, 'registration/article-create-update.html', context)
        