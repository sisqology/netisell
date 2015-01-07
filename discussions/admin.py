from django.contrib import admin
from discussions.models import Comment, Topic, Category


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'institution', 'user', 'date_created', 'active')
    inlines = [CommentInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'topic', 'user', 'date_created', 'active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)