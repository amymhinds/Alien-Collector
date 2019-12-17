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
    path('aliens/<int:alien_id>/add_testsubject/', views.add_testsubject, name='add_testsubject'),
    path('ufos/', views.UfoList.as_view(), name='ufos_index'),
    path('ufos/<int:pk>/', views.UfoDetail.as_view(), name='ufos_detail'),
    path('ufos/create/', views.UfoCreate.as_view(), name='ufos_create'),
    path('ufos/<int:pk>/update/', views.UfoUpdate.as_view(), name='ufos_update'),
    path('ufos/<int:pk>/delete/', views.UfoDelete.as_view(), name='ufos_delete'),
    path('aliens/<int:alien_id>/assoc_ufo/<int:ufo_id>/', views.assoc_ufo, name='assoc_ufo'),

]