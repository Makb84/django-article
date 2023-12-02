# from django import forms
# from .models import Article

# # from account.mixins import FieldsMixin

# class ArticleAddForm(forms.ModelForm):
#    class Meta:
#        model = Article
#        fields = '__all__' # Include all fields from the model

from django import forms
from .models import Article

class ArticleAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extract the 'fields' argument from kwargs
        fields_arg = kwargs.pop('fields', None)

        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

        # Update the 'fields' attribute based on the 'fields' argument
        if fields_arg:
            self.fields = {field_name: self.fields[field_name] for field_name in fields_arg}

    class Meta:
        model = Article
        fields = '__all__'  # Default fields option, can be overridden dynamically
