from django.urls import path 
from . import views

urlpatterns = [
    path('domace1/', views.domace1, name='domace1' ),
    path("du2_vizitka/", views.du2_vizitka, name="du2_vizitka"),
]