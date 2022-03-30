from django.contrib import admin

from .models import Quest

@admin.register(Quest)
class AdminQuest(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'