from django.shortcuts import render
from .models import Poke

from django.http import HttpResponse

# class Poke:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, poke_type, attack, level):
#     self.name = name
#     self.poke_type = poke_type
#     self.attack = attack
#     self.level = level

# poke = [
#   Poke('pikachu', 'electric', 'electro ball', 81),
#   Poke('charmander', 'fire', 'fire blast', 61),
#   Poke('wartortle', 'water', 'hydro pump', 93),
# ]
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def poke_index(request):
  poke = Poke.objects.all()
  return render(request, 'poke/index.html', { 'poke': poke })

def show(request,poke_id):
  pokemon = Poke.objects.get(id=poke_id)
  print(pokemon)
  return render(request, 'poke/show.html', {'pokemon': pokemon})