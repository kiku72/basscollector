from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bass, Amp
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
    # Exclude amps not associated with bass
    id_list = bass.amps.all().values_list('id')
    amps_bass_doesnt_have = Amp.objects.exclude(id__in=id_list)
    # instantiate StringsForm to be rendered in the details template
    string_form = StringForm()
    return render(request, 'basses/details.html', { 
        'bass':bass, 
        'amps': amps_bass_doesnt_have,
        'string_form': string_form 
    })


class BassCreate(CreateView):
    model = Bass
    fields = ['make', 'model', 'scale', 'color', 'construction']

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

class AmpCreate(CreateView):
    model = Amp
    fields = '__all__'

class AmpList(ListView):
    model = Amp
    fields = '__all__'

class AmpDetail(DetailView):
    model = Amp
    fields = '__all__'

class AmpDelete(DeleteView):
    model = Amp
    fields = '__all__'
    success_url = '/amps'

def assoc_amp(request, bass_id, amp_id):
    Bass.objects.get(id=bass_id).amps.add(amp_id)
    return redirect('bass_details', bass_id=bass_id)

def unassoc_amp(request, bass_id, amp_id):
    Bass.objects.get(id=bass_id).amps.remove(amp_id)
    return redirect('bass_details', bass_id=bass_id)