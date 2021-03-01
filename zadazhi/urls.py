from django.contrib import admin
from django.urls import path
from webapp.views import index_view, modern_view, modern_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),
    path('modern/add/', modern_create_view, name='create'),
    path('modern/<int:pk>/', modern_view, name='view')
]
