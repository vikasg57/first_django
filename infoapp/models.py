from django.db import models

# Create your models here.

class Info(models.Model):
    info_txt=models.CharField(max_length=300)

class Subinfo(models.Model):
    info=models.ForeignKey(Info,on_delete=models.CASCADE)
    
    subinfo_txt=models.CharField(max_length=300)