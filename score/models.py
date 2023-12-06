from django.db import models

# Create your models here.
    
class SummonerId(models.Model):
    summonerID = models.CharField(max_length=87)
    create_date = models.DateTimeField()

def __str__(self):
        return self.subject