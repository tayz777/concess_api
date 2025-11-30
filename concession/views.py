from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Concessionnaire, Vehicule
from .serializers import ConcessionnaireSerializer, VehiculeSerializer, UserSerializer


class UserCreateView(APIView):
    """
    Créer un nouvel utilisateur.
    POST /api/users/
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConcessionnaireListView(APIView):
    """
    Lister tous les concessionnaires.
    GET /api/concessionnaires/
    """

    def get(self, request):
        concessionnaires = Concessionnaire.objects.all()
        serializer = ConcessionnaireSerializer(concessionnaires, many=True)
        return Response(serializer.data)


class ConcessionnaireDetailView(APIView):
    """
    Afficher les détails d'un concessionnaire.
    GET /api/concessionnaires/<id>/
    """

    def get(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        serializer = ConcessionnaireSerializer(concessionnaire)
        return Response(serializer.data)


class VehiculeListView(APIView):
    """
    Lister les véhicules d'un concessionnaire.
    GET /api/concessionnaires/<id>/vehicules/
    """

    def get(self, request, concessionnaire_pk):
        # Vérifier que le concessionnaire existe
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicules = Vehicule.objects.filter(concessionnaire=concessionnaire)
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data)


class VehiculeDetailView(APIView):
    """
    Afficher les détails d'un véhicule spécifique.
    GET /api/concessionnaires/<id>/vehicules/<id>/
    """

    def get(self, request, concessionnaire_pk, pk):
        # Vérifier que le concessionnaire existe
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicule = get_object_or_404(
            Vehicule,
            pk=pk,
            concessionnaire=concessionnaire
        )
        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)

