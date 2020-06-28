from django.contrib import admin

from .models import Kategorija, Jelo


# Register your models here.

admin.site.register(Kategorija) # u admin panelu je dodana "Kategorija" za upravljanje
admin.site.register(Jelo) # u admin panelu je dodano "Jelo" za upravljanje