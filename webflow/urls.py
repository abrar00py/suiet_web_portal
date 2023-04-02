
from django.urls import path
from . import views


urlpatterns = [
    path('',views.webflowcommunity,name="webflowcommunity" ),
    path('sidharth',views.sidharth,name="sidharth" ),
    path('abrar',views.abrar,name="abrar" ),
    path('sam',views.sam,name="sam" ),
    path('shraddesh',views.shraddesh,name="shraddesh" ),
    path('sathwik',views.sathwik,name="sathwik" ),
    path('sujay',views.sujay,name="sujay" ),
    path('aditya',views.aditya,name="aditya" ),
    path('ammar',views.ammar,name="ammar" ),
    path('contact',views.contact,name="contact" ),
]
