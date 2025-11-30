# API Concessionnaire Auto/Moto

API REST Django pour la gestion d'un concessionnaire automobile et moto.

## Installation

```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## Lancement

```bash
# Appliquer les migrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver
```

## Endpoints

### Concessionnaires et Véhicules
- `GET /api/concessionnaires/` : Liste des concessionnaires
- `GET /api/concessionnaires/<id>/` : Détails d'un concessionnaire
- `GET /api/concessionnaires/<id>/vehicules/` : Véhicules d'un concessionnaire
- `GET /api/concessionnaires/<id>/vehicules/<id>/` : Détails d'un véhicule

### Authentification (Bonus)
- `POST /api/users/` : Création d'un utilisateur
- `POST /api/token/` : Obtention d'un token JWT
- `POST /api/refresh_token/` : Rafraîchissement du token JWT

