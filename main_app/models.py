from django.db import models

# Create your models here.
class Poke(models.Model):
    name = models.CharField(max_length=100)
    poke_type = models.CharField(max_length=100)
    attack = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name