from django import forms
from .models import Article

class ArticleAddForm(forms.ModelForm):
   class Meta:
       model = Article
       fields = '__all__' # Include all fields from the model