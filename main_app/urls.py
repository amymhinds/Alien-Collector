from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('aliens/', views.aliens_index, name='index'),
    path('aliens/<int:alien_id>/', views.aliens_detail, name='detail'),
    path('aliens/create/', views.AlienCreate.as_view(), name='aliens_create'),
    path('aliens/<int:pk>/update/', views.AlienUpdate.as_view(), name='aliens_update'),
    path('aliens/<int:pk>/delete/', views.AlienDelete.as_view(), name='aliens_delete'),
    path('alienes/<int:alien_id>/add_testsubject/', views.add_testsubject, name='add_testsubject'),
]