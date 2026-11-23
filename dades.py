inventari_bars = [
    {"id": 1, "nom": "El Racó del Born", "zona": "Born", "preu_tapa": 3.50, "aforament_actual": 38, "aforament_max": 50, "tapes_venudes": 140},
    {"id": 2, "nom": "Taverna Central Gràcia", "zona": "Gràcia", "preu_tapa": 2.80, "aforament_actual": 22, "aforament_max": 30, "tapes_venudes": 95},
    {"id": 3, "nom": "Craft & Tapes Poblenou", "zona": "Poblenou", "preu_tapa": 3.20, "aforament_actual": 15, "aforament_max": 40, "tapes_venudes": 160},
    {"id": 4, "nom": "Cerveseria de la Cantonada", "zona": "Sants", "preu_tapa": 2.50, "aforament_actual": 28, "aforament_max": 35, "tapes_venudes": 80},
    {"id": 5, "nom": "El Nou Bar Musical", "zona": "Raval", "preu_tapa": 3.00, "aforament_actual": 12, "aforament_max": 25, "tapes_venudes": 110}
]

def obtenir_tots_els_bars():
    return inventari_bars

def cercar_bar_per_id(id_buscat):
    for bar in inventari_bars:
        if bar["id"] == id_buscat:
            return bar
    return None

def filtrar_bars_per_zona(zona_cercada):
    coincidencies = []
    for bar in inventari_bars:
        if bar["zona"].lower() == zona_cercada.strip().lower():
            coincidencies.append(bar)
    return coincidencies

def actualitzar_dades_bar(id_bar, noves_persones, noves_tapes):
    bar = cercar_bar_per_id(id_bar)
    if bar:
        bar["aforament_actual"] += noves_persones
        bar["tapes_venudes"] += noves_tapes
        return True
    return False

def validar_disponibilitat(aforament_actual, persones, aforament_maxim):
    return (aforament_actual + persones) <= aforament_maxim