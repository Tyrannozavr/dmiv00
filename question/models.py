from django.db import models
from django.db.models import JSONField


class Quest(models.Model):
    form = JSONField()

    def __str__(self):
        return f'{self.form.get("form")}: {self.form.get("quest")}'
