from django.apps import AppConfig


class AccountConfig(AppConfig):

    # Specify the default auto field for models (Django 3.2+)    
    default_auto_field = 'django.db.models.BigAutoField'

    # Define the name of the app    
    name = 'account'
    
    # Set a custom verbose name for the app (displayed in the Django admin)
    verbose_name = 'اکانت'
