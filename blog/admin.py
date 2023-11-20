from django.contrib import admin
from .models import Article, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])  # Note: list_filter should be a tuple or list, not a set
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    def updated(self, obj):
        return obj.updated.strftime('%b %d, %Y %I:%M %p') if obj.updated else '-'

    updated.admin_order_field = 'updated'
    updated.short_description = 'Last Updated'

admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'created', 'updated', 'status', 'category_to_str')
    list_filter = ('publish', 'status',)  # Note: list_filter should be a tuple, not a set
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']

    def category_to_str(self,obj):
        # return "، ".join([category.title for category in obj.category.all()])
        return "، ".join([category.title for category in obj.category_published()])    
    category_to_str.short_description = "دسته بندی"


    def updated(self, obj):
        return obj.updated.strftime('%b %d, %Y %I:%M %p') if obj.updated else '-'

    updated.admin_order_field = 'updated'
    updated.short_description = 'Last Updated'

admin.site.register(Article, ArticleAdmin)


