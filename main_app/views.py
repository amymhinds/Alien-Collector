from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Alien, Ufo
from .forms import TestSubjectsForm

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
  testsubjects_form = TestSubjectsForm()
  ufos_alien_doesnt_have = Ufo.objects.exclude(id__in = alien.ufos.all().values_list('id'))
  return render(request, 'aliens/detail.html', { 'alien': alien,
   'testsubjects_form': testsubjects_form,
   'ufos': ufos_alien_doesnt_have})

def add_testsubject(request, alien_id):
  # create the ModelForm using the data in request.POST
  form = TestSubjectsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_testsubject = form.save(commit=False)
    new_testsubject.alien_id = alien_id
    new_testsubject.save()
  return redirect('detail', alien_id=alien_id)

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


class UfoList(ListView):
  model = Ufo

class UfoDetail(DetailView):
  model = Ufo

class UfoCreate(CreateView):
  model = Ufo
  fields = '__all__'

class UfoUpdate(UpdateView):
  model = Ufo
  fields = ['name', 'color']

class UfoDelete(DeleteView):
  model = Ufo
  success_url = '/ufos/'

def assoc_ufo(request, alien_id, ufo_id):
  # Note that you can pass a toy's id instead of the whole object
  Alien.objects.get(id=alien_id).ufos.add(ufo_id)
  return redirect('detail', alien_id=alien_id)