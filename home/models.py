from django.db import models

# Create your models here.
class Init(models.Model):
    project_author = models.CharField(max_length=25)
    project_year = models.IntegerField()

