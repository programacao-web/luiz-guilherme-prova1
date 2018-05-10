from django.db import models
from django.forms import ModelForm

# Create your models here.

LANGUAGE_CHOICES = (
    ('python', 'python'),
    ('javascript', 'javascript'),
    ('outros', 'outros')
)

class Paste(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)