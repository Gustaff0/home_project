from django.contrib import admin
from django.urls import path
from webapp.views import index_view, modern_view, modern_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('modern/add/', modern_create_view),
    path('modern/', modern_view)
]
