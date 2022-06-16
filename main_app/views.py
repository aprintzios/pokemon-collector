from django.shortcuts import render, redirect
from .models import Poke

from django.http import HttpResponse

import uuid
import boto3
from .models import Poke, Item, Photo

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'pokecollector'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def poke_index(request):
  poke = Poke.objects.all()
  return render(request, 'poke/index.html', { 'poke': poke })

def show(request,poke_id):
  pokemon = Poke.objects.get(id=poke_id)
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

def add_photo(request, poke_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, poke_id=poke_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect(f'/poke/{poke_id}')
