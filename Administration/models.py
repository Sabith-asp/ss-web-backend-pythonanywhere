from django.db import models

# Create your models here.
class ManagementCouncil(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='management council/')
    
    def __str__(self):
        return self.name
    
class DirectorBoard(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='director board/')
    
    def __str__(self):
        return self.name
    
class Chairman(models.Model):
    name = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='chairman/')
    
    def __str__(self):
        return self.name
    
class Manager(models.Model):
    name = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='manager/')
    
    def __str__(self):
        return self.name
    
class MCQA(models.Model):
    Description = models.TextField(max_length=100)
    Document = models.FileField(upload_to='mcqa/')
    
    def __str__(self):
        return self.Description
    
class MCQAmember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='mcqa/')
    
    def __str__(self):
        return self.name
    
class Principal(models.Model):
    name = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='manager/')
    
    def __str__(self):
        return self.name