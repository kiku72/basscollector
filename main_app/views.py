from django.shortcuts import render

# Create your views here.
basses = [
    {'make':'G&L', 'model':'SB2', 'scale':'34"', 'color': 'Sonic Blue', 'construction': 'Poplar body and maple/rosewood neck' },
    {'make':'Fender', 'model':'Jazz Bass', 'scale':'34"', 'color': 'Sunburst', 'construction': 'Basswood body and maple neck' },
    {'make':'Yamaha', 'model':'TRBX304', 'scale':'34"', 'color': 'Arctic White', 'construction': 'Mahogany body and maple/mahogany neck' },
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#we need to pass data, which we do with objects/dicts. this goes to the template!
def bass_index(request):
    return render(request, 'basses/index.html', {
        'basses' : basses
    })