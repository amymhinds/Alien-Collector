from django.db import models
from django.urls import reverse

# Create your models here.
class Alien(models.Model):
  name = models.CharField(max_length=100)
  planet = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
      return reverse('detail', kwargs={'alien_id': self.id})

class TestSubjects(models.Model):
  subject_type = models.CharField(max_length=50)
  experiment = models.CharField(max_length=50)

  alien = models.ForeignKey(Alien, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.experiment} on {self.subject_type}"


