from django.db import models
from datetime import datetime
from .profile import Profile



class CurriculumVitae(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    starting_date = models.DateField(default=datetime.strptime("1970-01-01", '%Y-%m-%d'))
    end_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))

class CurriculumVitaSection(models.Model):
    origin = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, null=False)
    starting_date = models.DateField(default=datetime.strptime("1970-01-01", '%Y-%m-%d'))
    end_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    content = models.TextField(max_length=255, null=False)