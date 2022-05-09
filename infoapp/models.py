from django.db import models

# Create your models here.

class Info(models.Model):
    #...    
    def __str__(self):  
        return self.info_txt
    info_txt=models.CharField(max_length=300)

class Subinfo(models.Model):
    #...
    def __str__(self):
        return self.subinfo_txt
    info=models.ForeignKey(Info,on_delete=models.CASCADE)

    subinfo_txt=models.CharField(max_length=300)