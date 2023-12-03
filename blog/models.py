from django.db import models
# from django.contrib.auth.models import User
from account.models import User
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_conventor

from django.urls import reverse


# my manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')
    
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.

class Category(models.Model):
    
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیردسته')
    title = models.CharField(max_length=200, verbose_name= "عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name= "آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود ؟")
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title
    
    objects = CategoryManager()



class Article(models.Model):
    STATUS_CHOICES = (

        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')

    )

    # Fields for the Article model
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='articles', verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name= "عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name= "آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    description = models.TextField(verbose_name= "متن")
    thumbnail = models.ImageField(upload_to="images", verbose_name= "تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name= "زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,default='d',null=True, blank=True, choices=STATUS_CHOICES, verbose_name= "وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
    
    
    # Methods for the Article model

    def __str__(self):
        return self.title
    
    def jpublish(self):

        return jalali_conventor(self.publish)
    
    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)
    
    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px' src='{}'>".format(self.thumbnail.url))
    
    thumbnail_tag.short_description = "عکس"

    def category_to_str(self):
        # return "، ".join([category.title for category in obj.category.all()])
        return "، ".join([category.title for category in self.category_published()])    
    category_to_str.short_description = "دسته بندی"

    def get_absolute_url(self):
        return reverse("account:home")
    
    
    # Associate the custom manager with the Article model

    objects = ArticleManager()
