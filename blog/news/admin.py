from django.contrib import admin
from .models import Articles


class AdminArticles(admin.ModelAdmin):
    list_display = ('title', 'full_text', 'author', 'date')


admin.site.register(Articles, AdminArticles)
