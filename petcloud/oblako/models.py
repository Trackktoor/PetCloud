from django.contrib.auth.models import User
from django.db import models

class Files(models.Model):
    # Koshernost = [
    #     ('xxxx', 'zbs! ogon!'),
    #     ('xxx', 'opasen'),
    #     ('xx', 'normul'),
    #     ('x', 'shliapa'),
    # ]
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=600, null=True, blank=True)
    media = models.FileField(null=True, blank=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
