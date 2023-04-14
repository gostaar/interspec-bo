from django.db import models


# Create your models here.


class Editeur(models.Model):
    nom = models.CharField(max_length=250)

class Auteur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)

class Genre(models.Model):
    nom = models.CharField(max_length=250)

class Livre(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    isbn = models.CharField(max_length=250)
    archive = models.BooleanField
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

class Stock(models.Model):
    emplacement = models.CharField(max_length=250)

class Usure(models.Model):
    nom = models.CharField(max_length=250)

class Exemplaire(models.Model):
    book = models.ForeignKey(Livre, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    usure = models.ForeignKey(Usure, on_delete=models.CASCADE)

class Adherent(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)
    email = models.EmailField
    caution = models.BooleanField

class emprunt(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE)
    date_emprunt = models.DateField
    date_retour = models.DateField
    status = models.CharField(max_length=250)