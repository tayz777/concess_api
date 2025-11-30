from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Concessionnaire, Vehicule


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer pour la création d'utilisateur.
    Le mot de passe est en write_only pour la sécurité.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # create_user pour hacher le mot de passe
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class ConcessionnaireSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Concessionnaire.
    Le champ 'siret' est exclu pour ne pas être exposé par l'API.
    """

    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom']  


class VehiculeSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Véhicule.
    Tous les champs sont inclus.
    """

    class Meta:
        model = Vehicule
        fields = ['id', 'type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire']

