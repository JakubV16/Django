from django.urls import path 
from . import views

urlpatterns = [
    path('domace1/', views.domace1, name='domace1' ),
]