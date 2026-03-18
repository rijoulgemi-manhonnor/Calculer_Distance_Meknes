import os

# Récupère la clé depuis les secrets GitHub ou utilise une valeur par défaut
ORS_API_KEY = os.getenv("ORS_API_KEY", "VOTRE_CLE_API_ICI") 

MEKNES_COORDS = {
    "name": "Meknès",
    "lat": 33.8935,
    "lon": -5.5473
}

REQUEST_DELAY = 1.5
OUTPUT_FILENAME = "distances_meknes_communes_fes_meknes.xlsx"
OUTPUT_DIR = "output"
