import os
import pandas as pd
from datetime import datetime
from config import OUTPUT_FILENAME, OUTPUT_DIR
from communes import get_all_communes
from distance_calculator import DistanceCalculator

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    communes = get_all_communes(include_rural=True)
    calculator = DistanceCalculator()
    results = []

    print(f"Démarrage du calcul pour {len(communes)} communes...")

    for c in communes:
        lat, lon = calculator.geocode_commune(c["search_name"])
        dist, dur = (None, None)
        if lat:
            time.sleep(1) # Respecter les limites API
            dist, dur = calculator.calculate_route_distance(lat, lon)
        
        results.append({
            "Commune": c["name"],
            "Province": c["province"],
            "Distance (km)": dist,
            "Durée (min)": dur,
            "Statut": "✅" if dist else "❌"
        })

    df = pd.DataFrame(results)
    filepath = os.path.join(OUTPUT_DIR, f"distances_meknes_{datetime.now().strftime('%Y%m%d')}.xlsx")
    df.to_excel(filepath, index=False)
    print(f"Fichier sauvegardé : {filepath}")

if __name__ == "__main__":
    import time
    main()
