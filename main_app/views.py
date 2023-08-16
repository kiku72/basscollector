from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bass
from .forms import StringForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# we need to pass data, which we do with objects/dicts. this goes to the template!
def bass_index(request):
    basses = Bass.objects.all()
    return render(request, 'basses/index.html', {
        'basses' : basses
    })

def bass_details(request, bass_id):
    bass = Bass.objects.get(id=bass_id)
    # instantiate StringsForm to be rendered in the details template
    string_form = StringForm()
    return render(request, 'basses/details.html', { 'bass':bass, 'string_form': string_form })

class BassCreate(CreateView):
    model = Bass
    fields = '__all__'

class BassUpdate(UpdateView):
    model = Bass
    fields = '__all__'

class BassDelete(DeleteView):
    model = Bass
    success_url = '/basses'

def add_string(request, bass_id):
    form = StringForm(request.POST)
    if form.is_valid():
        new_string = form.save(commit=False)
        new_string.bass_id = bass_id
        new_string.save()
    return redirect('bass_details', bass_id=bass_id)