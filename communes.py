COMMUNES = [
    {"name": "Meknès", "province": "Préfecture de Meknès", "type": "Urbaine", "search_name": "Meknès, Morocco"},
    {"name": "Ouislane", "province": "Préfecture de Meknès", "type": "Urbaine", "search_name": "Ouislane, Meknès, Morocco"},
    {"name": "Toulal", "province": "Préfecture de Meknès", "type": "Urbaine", "search_name": "Toulal, Meknès, Morocco"},
    {"name": "Boufekrane", "province": "Préfecture de Meknès", "type": "Urbaine", "search_name": "Boufekrane, Morocco"},
    {"name": "Fès", "province": "Préfecture de Fès", "type": "Urbaine", "search_name": "Fès, Morocco"},
    {"name": "El Hajeb", "province": "El Hajeb", "type": "Urbaine", "search_name": "El Hajeb, Morocco"},
    {"name": "Ifrane", "province": "Ifrane", "type": "Urbaine", "search_name": "Ifrane, Morocco"},
    {"name": "Azrou", "province": "Ifrane", "type": "Urbaine", "search_name": "Azrou, Morocco"},
    {"name": "Sefrou", "province": "Sefrou", "type": "Urbaine", "search_name": "Sefrou, Morocco"},
    {"name": "Missour", "province": "Boulemane", "type": "Urbaine", "search_name": "Missour, Morocco"},
    {"name": "Taounate", "province": "Taounate", "type": "Urbaine", "search_name": "Taounate, Morocco"},
    {"name": "Taza", "province": "Taza", "type": "Urbaine", "search_name": "Taza, Morocco"},
    {"name": "Guercif", "province": "Guercif", "type": "Urbaine", "search_name": "Guercif, Morocco"}
]

COMMUNES_RURALES = [
    {"name": "Dkhissa", "province": "Préfecture de Meknès", "type": "Rurale", "search_name": "Dkhissa, Meknès, Morocco"},
    {"name": "Ain Leuh", "province": "Ifrane", "type": "Rurale", "search_name": "Ain Leuh, Morocco"},
    {"name": "Guigou", "province": "Boulemane", "type": "Rurale", "search_name": "Guigou, Morocco"}
]

def get_all_communes(include_rural=True):
    if include_rural:
        return COMMUNES + COMMUNES_RURALES
    return COMMUNES
