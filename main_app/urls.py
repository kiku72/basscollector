from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('basses/', views.bass_index, name="bass_index"),
    path('basses/<int:bass_id>', views.bass_details, name="bass_details"),
    path('basses/create/', views.BassCreate.as_view(), name="bass_create"),
    path('basses/<int:pk>/update/', views.BassUpdate.as_view(), name="bass_update"),
    path('basses/<int:pk>/delete/', views.BassDelete.as_view(), name='bass_delete'),
    path('basses/<int:bass_id>/add_string/', views.add_string, name='add_string'),
]