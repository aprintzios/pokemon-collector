from django.contrib import admin

# Register your models here.
from .models import Poke, Item, Photo, Attack

# Register your models here
admin.site.register(Poke)
admin.site.register(Item)
admin.site.register(Photo)
admin.site.register(Attack)