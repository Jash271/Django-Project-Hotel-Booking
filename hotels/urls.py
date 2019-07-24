from django.contrib import admin
from django.urls import include, path
from .  import views


urlpatterns = [
     path('',views.room,name='room'),
     path("search",views.search,name='search'),
     path("book",views.book,name='book'),
     path("confirm",views.confirm,name='confirm'),
     path("pay",views.pay,name='pay')
    
    
]
