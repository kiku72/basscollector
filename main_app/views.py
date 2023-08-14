from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bass

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#we need to pass data, which we do with objects/dicts. this goes to the template!
def bass_index(request):
    basses = Bass.objects.all()
    return render(request, 'basses/index.html', {
        'basses' : basses
    })

def bass_details(request, bass_id):
    bass = Bass.objects.get(id=bass_id)
    return render(request, 'basses/details.html', { 'bass':bass })

class BassCreate(CreateView):
    model = Bass
    fields = '__all__'

class BassUpdate(UpdateView):
    model = Bass
    fields = '__all__'

class BassDelete(DeleteView):
    model = Bass
    success_url = '/basses'