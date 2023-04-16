from django.contrib import admin

# Register your models here.
from .models import Editeur, Auteur, Genre, Livre, Stock, Usure, Exemplaire, Adherent, Emprunt

admin.site.register(Editeur)
admin.site.register(Auteur)
admin.site.register(Genre)
admin.site.register(Livre)
admin.site.register(Stock)
admin.site.register(Usure)
admin.site.register(Exemplaire)
admin.site.register(Adherent)
admin.site.register(Emprunt)
