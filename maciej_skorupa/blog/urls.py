from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('solo', views.solo, name='solo'),
    path('bohomaz', views.bohomaz, name='bohomaz'),
    path('petla', views.petla, name='petla'),
    path('kontakt', views.kontakt, name='kontakt'),
]
