# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path
from .views import home, article_create, article_update, article_delete

# Set the app namespace for reverse URL patterns
app_name = 'account'

urlpatterns = [
    # -----Login view using Django's built-in LoginView-----
    path("login/", views.LoginView.as_view(), name="login"),

    # -----Other authentication-related views (commented out for simplicity)-----
    
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    # ),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]


urlpatterns += [
    # Home view for the 'account' app
    path('', home, name="home"),
    # View to create an article in the 'account' app
    path('article/create', article_create, name="article-create"),
    path('article/update/<slug:slug>', article_update, name="article-update"),
    path('article/delete/<slug:slug>', article_delete, name="article-delete"),

]