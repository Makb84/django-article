from django.urls import path
# from .views import home, api
from .views import home, detail

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    # path('api', api, name='api')
    # path('article/<slug:slug>', detail_article, name='detail_article')
    path('article/<slug:slug>', detail, name='detail')

]