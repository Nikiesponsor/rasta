from django.db import models

# Create your models here.


class Album(models.Model):
    nom_Album=models.CharField(max_length=100)
    pochette=models.FileField(upload_to='pochette',help_text="pochette de l album",blank=True)
    desciption=models.TextField(blank=True)
    
    def __str__(self):
        return self.nom_Album

class Titre(models.Model):
    nom_titre=models.CharField(max_length=100)
    feat=models.CharField(max_length=100,blank=True)
    descp=models.TextField(blank=True)
    Album=models.ForeignKey(Album,on_delete=models.CASCADE,related_name='album')
    def __str__(self):
        return  self.nom_titre

class Single(models.Model):
    non_single=models.CharField(max_length=100)
    pochette_single=models.FileField(upload_to='pochette_single',help_text="pochette du single",blank=True)
    def __str__(self):
        return self.non_single

class Evenements(models.Model):
    nom_evenement=models.CharField(max_length=100)
    imgages=models.FileField(upload_to='imagesEvenements',help_text="images de l evenements")
    def __str__(self):
        return  self.nom_evenement