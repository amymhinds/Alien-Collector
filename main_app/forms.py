from django.forms import ModelForm
from .models import TestSubjects

class TestSubjectsForm(ModelForm):
  class Meta:
    model = TestSubjects
    fields = ['experiment', 'subject_type']