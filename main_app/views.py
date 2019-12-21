from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Alien, Ufo, Photo
from .forms import TestSubjectsForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-amh'

# Create your views here.
def home(request):
  return HttpResponse('<h1>Greetings Earthlings >-)</h1>')

def about(request):
  return render(request, 'about.html')

@login_required
def aliens_index(request):
  aliens = Alien.objects.filter(user=request.user)
  return render(request, 'aliens/index.html', { 'aliens': aliens })


@login_required
def aliens_detail(request, alien_id):
  alien = Alien.objects.get(id=alien_id)
  testsubjects_form = TestSubjectsForm()
  ufos_alien_doesnt_have = Ufo.objects.exclude(id__in = alien.ufos.all().values_list('id'))
  return render(request, 'aliens/detail.html', { 'alien': alien,
   'testsubjects_form': testsubjects_form,
   'ufos': ufos_alien_doesnt_have})

@login_required
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

class AlienCreate(LoginRequiredMixin, CreateView):
  model = Alien
  fields = ['name', 'planet', 'description', 'age']
    # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)




class AlienUpdate(LoginRequiredMixin, UpdateView):
  model = Alien
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['planet', 'description', 'age']

class AlienDelete(LoginRequiredMixin, DeleteView):
  model = Alien
  success_url = '/aliens/'


class UfoList(LoginRequiredMixin, ListView):
  model = Ufo

class UfoDetail(LoginRequiredMixin, DetailView):
  model = Ufo

class UfoCreate(LoginRequiredMixin, CreateView):
  model = Ufo
  fields = '__all__'

class UfoUpdate(LoginRequiredMixin, UpdateView):
  model = Ufo
  fields = ['name', 'color']

class UfoDelete(LoginRequiredMixin, DeleteView):
  model = Ufo
  success_url = '/ufos/'

@login_required
def assoc_ufo(request, alien_id, ufo_id):
  # Note that you can pass a toy's id instead of the whole object
  Alien.objects.get(id=alien_id).ufos.add(ufo_id)
  return redirect('detail', alien_id=alien_id)

@login_required
def add_photo(request, alien_id):
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
            photo = Photo(url=url, alien_id=alien_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', alien_id=alien_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)