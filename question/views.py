from django.shortcuts import render
from .forms import Quest

def index(request):
    quest2 = Quest()
    quest2.initial['form'] = 'form2'
    form = [quest2]
    if request.POST:
        print(request.POST)
        # print(request.POST.get('quest'))
        # print(request.POST.get('form'))
    return render(request, 'question/index.html', {'forms': form})
