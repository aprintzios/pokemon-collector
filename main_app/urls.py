from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('poke/', views.poke_index, name='index'),
  path('poke/<int:poke_id>/', views.show, name='show'),
]