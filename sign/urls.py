from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('',views.signup , name='signup'),
    # path('signin',views.signin , name='signin'),

]
