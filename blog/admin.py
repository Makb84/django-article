from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'created', 'updated', 'status')
    list_filter = ('publish', 'status',)  # Note: list_filter should be a tuple, not a set
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']

    def updated(self, obj):
        return obj.updated.strftime('%b %d, %Y %I:%M %p') if obj.updated else '-'

    updated.admin_order_field = 'updated'
    updated.short_description = 'Last Updated'

admin.site.register(Article, ArticleAdmin)