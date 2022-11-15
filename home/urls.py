from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('category', views.category, name='catogory'),    
    path('single', views.single, name='single'),    
    path('contact', views.contact, name='contact'),
]
