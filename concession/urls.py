from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    ConcessionnaireListView,
    ConcessionnaireDetailView,
    VehiculeListView,
    VehiculeDetailView,
    UserCreateView,
)

urlpatterns = [
    # Routes pour les concessionnaires
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    
    # Routes pour les véhicules
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/', VehiculeListView.as_view(), name='vehicule-list'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:pk>/', VehiculeDetailView.as_view(), name='vehicule-detail'),
    
    # Routes pour l'authentification JWT
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token-refresh'),
]

