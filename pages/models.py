from django.db import models
from datetime import datetime

# Create your models here.

class Expert(models.Model):
    name            =   models.CharField(max_length=255)
    designation     =   models.CharField(blank=True, max_length=255)
    linkedin        =   models.URLField(max_length=100)
    headshot        =   models.ImageField(upload_to="photos/%Y/%m/%d")   
    company1        =   models.ImageField(blank=True, upload_to="photos/%Y/%m/%d")   
    company2        =   models.ImageField(blank=True, upload_to="photos/%Y/%m/%d")   
    created_at      =   models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name