from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User


class Facultad(models.Model):
    id_Facultad = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('era:facultad_details', kwargs={'pk': self.pk})


class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=45)
    abreviado = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    Facultad_idFacultad = models.ForeignKey(Facultad, on_delete= models.CASCADE,default="1")
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('era:career_details', kwargs={
            'pk': self.Facultad_idFacultad.id_Facultad,
            'pkr': self.pk,
        })

    def get_facultad(self):
        return Facultad.objects.get(pk=self.Facultad_idFacultad.pk)
