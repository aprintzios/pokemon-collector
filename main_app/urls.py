from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('poke/', views.poke_index, name='index'),
  path('poke/new/', views.new, name='new'),
  path('poke/<int:poke_id>/', views.show, name='show'),
  path('poke/submit/', views.submit, name='submit'),
  path('poke/<int:poke_id>/edit', views.edit, name='edit'),
  path('poke/<int:poke_id>/update', views.update, name='update'),
  path('poke/<int:poke_id>/delete', views.delete, name='delete'),
  path('poke/<int:poke_id>/add_photo/', views.add_photo, name='add_photo'),
]