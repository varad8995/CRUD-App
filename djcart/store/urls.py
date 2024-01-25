from django.contrib import admin
from django.urls import path
from store.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('cart',cart)
]