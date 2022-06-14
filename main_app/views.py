from django.shortcuts import render, redirect
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

def new(request):
  return render(request, 'poke/new.html')

def submit(request):
  print(request.POST)
  poke = Poke.objects.create(
    name=request.POST['name'],
    poke_type=request.POST['type'],
    attack=request.POST['attack'],
    level=request.POST['level']
    )
  return redirect('/poke')

def edit(request, poke_id):
  poke = Poke.objects.get(id=poke_id)
  return render(request, 'poke/edit.html', {'poke': poke})

def update(request, poke_id):
    poke = Poke.objects.get(id=poke_id)
    poke.name=request.POST['name']
    poke.poke_type=request.POST['type']
    poke.attack=request.POST['attack']
    poke.level=request.POST['level']
    poke.save()
    return redirect(f'/poke/{poke_id}')
  
def delete(request, poke_id):
  Poke.objects.filter(id=poke_id).delete()
  return redirect('/poke')