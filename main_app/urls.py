from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('aliens/', views.aliens_index, name='index'),
    path('aliens/<int:alien_id>/', views.aliens_detail, name='detail'),
]