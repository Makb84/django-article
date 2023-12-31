from django.urls import path
# from .views import home, api
from .views import home, detail, category, author

app_name = 'blog'

urlpatterns = [
    
    path('', home, name='home'),
    path('page/<int:page_number>', home, name='home'),
    # path('api', api, name='api')
    # path('article/<slug:slug>', detail_article, name='detail_article')
    path('article/<slug:slug>', detail, name='detail'),
    path('category/<slug:slug>', category, name='category'),
    path('author/<slug:username>', author, name='author'),

]