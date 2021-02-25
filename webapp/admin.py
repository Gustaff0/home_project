from django.contrib import admin
from webapp.models import Modern

# Register your models here.

class ModernAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'time']
    list_filter = ['status']
    search_fields = ['title', 'time']
    fields = ['id', 'title', 'author', 'content']


admin.site.register(Modern, ModernAdmin)
