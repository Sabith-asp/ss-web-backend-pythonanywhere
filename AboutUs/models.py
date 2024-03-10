from django.db import models

# Create your models here.
class MissionVision(models.Model):
    mission = models.CharField(max_length=100)
    vision = models.CharField(max_length=100)
    Corevalues = models.CharField(max_length=50)
    
    def __str__(self):
        return self.mission

    
    
class HistoryofCollege(models.Model):
    Description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='history/')
    
    def __str__(self):
        return self.Description
    
class AboutCollege(models.Model):
    Description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='aboutcollege/')
    
    def __str__(self):
        return self.Description
    
class SisterInstituition(models.Model):
    name = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)
    Address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sisterInstituition/')
    
    def __str__(self):
        return self.name
    
class FormerPrincipal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    year = models.CharField(max_length=20)
    image = models.ImageField(upload_to='formerprincipal/')
    
    def __str__(self):
        return self.name
    
class Accreditation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='accreditation/')
    
    def __str__(self):
        return self.name
    
class RecognitionandAward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='recognitionandaward/')
    
    def __str__(self):
        return self.name
    
class StrategicPlan(models.Model):
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='strategicplan/')
    
    def __str__(self):
        return self.name
    
class RTI(models.Model):
    document = models.FileField(upload_to='rti/')
    
    def __str__(self):
        return self.document
