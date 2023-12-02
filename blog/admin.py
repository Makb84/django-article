from django.contrib import admin
from .models import Article, Category

from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.

# admin.site.disable_action("delete_selected")

# Custom admin actions for bulk updating article status
@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status="p")
    modeladmin.message_user(
        request,
        ngettext(
            "%d مقاله با موفقیت انتشار یافت",
            "%d مقاله با موفقیت انتشار یافت",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(description="پیش نویس شدن مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status="d")
    modeladmin.message_user(
        request,
        ngettext(
            "%d مقاله به حالت پیش نویس درآمد",
            "%d مقاله به حالت پیش نویس درآمد",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


class CategoryAdmin(admin.ModelAdmin):
    # Configuration for Category model in admin panel
    
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])  # Note: list_filter should be a tuple or list, not a set
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    def updated(self, obj):
        return obj.updated.strftime('%b %d, %Y %I:%M %p') if obj.updated else '-'

    updated.admin_order_field = 'updated'
    updated.short_description = 'Last Updated'

admin.site.register(Category, CategoryAdmin)

# Register the Category model with the custom admin configuration
class ArticleAdmin(admin.ModelAdmin):
    # Configuration for Article model in admin panel

    list_display = ('title', 'thumbnail_tag', 'slug', 'author', 'jpublish', 'created', 'updated', 'status', 'category_to_str')
    list_filter = ('publish', 'status',)  # Note: list_filter should be a tuple, not a set
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']
    actions = [make_published, make_draft]    

    def category_to_str(self,obj):
        # Return a string representation of the categories associated with the article        

        # return "، ".join([category.title for category in obj.category.all()])
        return "، ".join([category.title for category in obj.category_published()])    
    category_to_str.short_description = "دسته بندی"


    def updated(self, obj):
        return obj.updated.strftime('%b %d, %Y %I:%M %p') if obj.updated else '-'

    updated.admin_order_field = 'updated'
    updated.short_description = 'Last Updated'

# Register the Article model with the custom admin configuration
admin.site.register(Article, ArticleAdmin)


