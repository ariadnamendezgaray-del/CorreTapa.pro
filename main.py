"""
interficie.py
Funcions que mostren el menú i demanen dades a l'usuari.
"""
from config import NOM_ESDEVENIMENT, VERSIO, MSG_EXIT_RESERVA, MAX_PERSONES_RESERVA, MSG_OPCIO_INVALIDA
import logica 
import main



def zona_no_encontrada(zona):
    print(f"❌ No s'ha trobat cap bar a '{zona}'.")
def no_existe():
    print("❌ No existeix aquest bar.")
def error_aforament():
    print(MSG_ERROR_AFORAMENT)

def despedida():
    print(f"\nGràcies per utilitzar {NOM_ESDEVENIMENT}. Fins aviat!")
def no_valida():
    print(MSG_OPCIO_INVALIDA)


def mostrar_benvinguda():
    print("=" * 55)
    print(f"🌟  {NOM_ESDEVENIMENT} (v{VERSIO})")
    print("=" * 55)

def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Catàleg de bars i preus")
    print("2. Cercar bars per zona")
    print("3. Reservar taula i demanar tapes")
    print("4. Estadístiques de la xarxa")
    print("0. Sortir")

def demanar_opcio():
    return input("\n👉 Selecciona una opció: ").strip()

def mostrar_carta_bars(llista):
    print("\n📍 LOCALS DISPONIBLES:")
    for b in llista:
        lliures = b["aforament_max"] - b["aforament_actual"]
        print(f"  [{b['id']}] {b['nom']:<26} | {b['zona']:<9} | {b['preu_tapa']:.2f}€ | Lliures: {lliures}")

def demanar_zona_cerca():
    return input("\n👉 Introdueix la zona a cercar: ").strip()

def demanar_dades_reserva():
    try:
        id_bar = int(input("\n👉 ID del bar: "))
        persones = int(input("👉 Nombre de persones: "))
        tapes = int(input("👉 Nombre de tapes: "))
        soci = input("👉 Ets soci/a del festival? (s/n): ").strip().lower() == "s"
        if persones <= 0 or persones > MAX_PERSONES_RESERVA or tapes <= 0:
            print("❌ Valors fora de rang permès.")
            return None
        return {"id_bar": id_bar, "persones": persones, "tapes": tapes, "es_soci": soci}
    except ValueError:
        print("❌ Error: Cal introduir valors numèrics enters.")
        return None

def mostrar_resum_comanda(bar, reserva, detall):
    print("\n" + "=" * 45)
    print(f"🧾 REBUT DE RESERVA: {bar['nom'].upper()}")
    print("-" * 45)
    print(f"Persones: {reserva['persones']} | Tapes: {reserva['tapes']}")
    print(f"Subtotal: {detall['subtotal_brut']:.2f}€ | Descompte: -{detall['descompte']:.2f}€")
    print(f"Base: {detall['base_imposable']:.2f}€ | IVA (10%): {detall['iva']:.2f}€")
    print("-" * 45)
    print(f"💰 TOTAL: {detall['total']:.2f}€")
    print("=" * 45)
    print(MSG_EXIT_RESERVA)

def mostrar_panell_estadistiques(stats):
    if not stats:
        print("❌ No hi ha dades suficients.")
        return
    print("\n📊 ESTADÍSTIQUES DEL CIRCUIT:")
    print(f"  • Total bars: {stats['num_bars']} | Tapes venudes: {stats['total_tapes']}")
    print(f"  • Preu mitjà: {stats['preu_mitja']:.2f}€ | Més popular: {stats['bar_popular']}")