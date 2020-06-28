import datetime

from django.db import models

from django.utils import timezone

# Create your models here.

class Kategorija(models.Model):
    ime_kategorije = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.ime_kategorije

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Jelo(models.Model):
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    naziv_jela = models.CharField(max_length=200)
    broj_kalorija = models.IntegerField(default=0)

    def __str__(self):
        return self.naziv_jela