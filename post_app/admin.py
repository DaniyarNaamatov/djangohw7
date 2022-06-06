from django.contrib import admin
from .models import News, NewsComment, Tag

class CommentInline(admin.StackedInline):
    model = NewsComment
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = 'title text'.split()
    list_filter = 'created_at tags'.split()
    inlines = [CommentInline]



admin.site.register(News, NewsAdmin)
admin.site.register(NewsComment)
admin.site.register(Tag)



