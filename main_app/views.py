from django.shortcuts import render

from django.http import HttpResponse

class Poke:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, poke_type, attack, level):
    self.name = name
    self.poke_type = poke_type
    self.attack = attack
    self.level = level

poke = [
  Poke('pikachu', 'electric', 'electro ball', 81),
  Poke('charmander', 'fire', 'fire blast', 61),
  Poke('wartortle', 'water', 'hydro pump', 93),
]
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def poke_index(request):
  return render(request, 'poke/index.html', { 'poke': poke })
