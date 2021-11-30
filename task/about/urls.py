from django.urls import path
from about.views import *

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', photo, name='gallery'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts')
]