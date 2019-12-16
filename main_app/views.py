from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Alien


# class Alien:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, planet, description, age):
#     self.name = name
#     self.planet = planet
#     self.description = description
#     self.age = age

#     def __str__(self):
#         return self.name

# Create your views here.
def home(request):
  return HttpResponse('<h1>Greetings Earthlings >-)</h1>')

def about(request):
  return render(request, 'about.html')

def aliens_index(request):
  aliens = Alien.objects.all()
  return render(request, 'aliens/index.html', { 'aliens': aliens })


def aliens_detail(request, alien_id):
  alien = Alien.objects.get(id=alien_id)
  return render(request, 'aliens/detail.html', { 'alien': alien })

class AlienCreate(CreateView):
  model = Alien
  fields = '__all__'
  success_url = '/aliens/'

class AlienUpdate(UpdateView):
  model = Alien
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['planet', 'description', 'age']

class AlienDelete(DeleteView):
  model = Alien
  success_url = '/aliens/'