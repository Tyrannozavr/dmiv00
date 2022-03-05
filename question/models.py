from django.db import models
from django.db.models import JSONField

class Quest(models.Model):
    # quest = models.CharField(max_length=255)
    form = JSONField()

    def __str__(self):
        # return self.form
        return f'{self.form.get("form")}: {self.form.get("quest")}'
