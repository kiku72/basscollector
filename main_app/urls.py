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

    path('basses/<int:bass_id>/assoc_amp/<int:amp_id>/', views.assoc_amp, name='assoc_amp'),
    path('basses/<int:bass_id>/unassoc_amp/<int:amp_id>/', views.unassoc_amp, name='unassoc_amp'),

    path('amps/', views.AmpList.as_view(), name="amp_index"),
    path('amps/<int:pk>/', views.AmpDetail.as_view(), name="amp_detail"),
    path('amps/create/', views.AmpCreate.as_view(), name="amp_create"),
    path('amps/<int:pk>/delete/', views.AmpDelete.as_view(), name="amp_delete"),
]