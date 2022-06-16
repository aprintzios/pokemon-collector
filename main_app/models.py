from django.db import models

# Create your models here.
class Poke(models.Model):
    name = models.CharField(max_length=100)
    poke_type = models.CharField(max_length=100)
    attack = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name
        

class Item(models.Model):
  name = models.CharField(max_length=100)
  poke = models.ForeignKey(Poke, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

class Photo(models.Model):
    url = models.CharField(max_length=200)
    poke = models.ForeignKey(Poke, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for poke_id: {self.poke_id} @{self.url}"