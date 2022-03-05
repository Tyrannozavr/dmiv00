from django.shortcuts import render
from .forms import Quest, Add
from .models import Quest as quest_model


count = 1
def index(request):
    global count
    if request.POST:
        if request.POST.get('add'):
            count += 1
        if request.POST.get('quest'):
            a = dict(request.POST)
            quest = a.get('quest')
            form = a.get('form')
            quest_form = zip(quest, form)
            for quest, form in quest_form:
                print(len(quest))
                if quest:
                    quest_model.objects.create(form={'quest': quest, 'form': form})
                print(quest, form)
            # print(list(quest_form))
    if request.method == 'GET':
        count = 1
    add = Add()
    quests = []
    for i in range(count):
        a = Quest()
        a.initial['form'] = f'form{i}'
        quests.append(a)
    return render(request, 'question/index.html', {'forms': quests, 'add': add})
