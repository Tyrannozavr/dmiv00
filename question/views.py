from django.shortcuts import render
from django.views.generic import ListView

from .forms import Add, Quest
from .models import Quest as quest_model

count = 1
def index(request):
    global count
    if request.POST:
        print(request.POST)
        if request.POST.get('add'):
            count += 1
        if request.POST.get('quest'):
            a = dict(request.POST)
            quest = a.get('quest')
            form = a.get('form')
            quest_form = zip(quest, form)
            for quest, form in quest_form:
                if quest:
                    quest_model.objects.create(form={'quest': quest, 'form': form})
    if request.method == 'GET':
        count = 1
    add = Add()
    quests = []
    for i in range(count):
        a = Quest()
        a.initial['form'] = f'form{i}'
        quests.append(a)
    return render(request, 'question/index.html', {'forms': quests, 'add': add})

class List_quests(ListView):
    model = quest_model

