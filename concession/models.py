from django.db import models
from django.core.validators import MinLengthValidator


class Concessionnaire(models.Model):
    """
    Modèle représentant un concessionnaire automobile/moto.
    Le SIRET est stocké mais non exposé par l'API.
    """
    nom = models.CharField(max_length=64)
    siret = models.CharField(
        max_length=14,
        validators=[MinLengthValidator(14)]
    )

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Concessionnaire"
        verbose_name_plural = "Concessionnaires"


class Vehicule(models.Model):
    """
    Modèle représentant un type de véhicule appartenant à un concessionnaire.
    """
    TYPE_CHOICES = [
        ('moto', 'Moto'),
        ('auto', 'Auto'),
    ]

    concessionnaire = models.ForeignKey(
        Concessionnaire,
        on_delete=models.CASCADE,
        related_name='vehicules'
    )
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=64)
    chevaux = models.IntegerField()
    prix_ht = models.FloatField()

    def __str__(self):
        return f"{self.marque} ({self.type})"

    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"

