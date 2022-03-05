from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('quests/', List_quests.as_view(), name='list')
]