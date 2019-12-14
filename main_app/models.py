from django.db import models

# Create your models here.
class Alien(models.Model):
  name = models.CharField(max_length=100)
  planet = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  
  def __str__(self):
    return f'{self.name} ({self.id})'
