import dades
import interface
import config  



def calcular_descompte(subtotal, quantitat_persones, es_soci):
    print(">> Verificant promocions aplicables a la comanda...")
    if es_soci:
        return subtotal * DESCOMPTE_SOCI
    elif quantitat_persones >= MIN_PERSONES_GRUP:
        return subtotal * DESCOMPTE_GRUP
    return 0.0

def calcular_total_comanda(preu_tapa, quantitat_tapes, quantitat_persones, es_soci):
    print(">> Calculant import econòmic amb desglossament d'IVA...")
    subtotal_brut = preu_tapa * quantitat_tapes
    import_descompte = calcular_descompte(subtotal_brut, quantitat_persones, es_soci)
    base_imposable = subtotal_brut - import_descompte
    quota_iva = base_imposable * IVA_HOSTALERIA
    total_final = base_imposable + quota_iva
    return {
        "subtotal_brut": round(subtotal_brut, 2), "descompte": round(import_descompte, 2),
        "base_imposable": round(base_imposable, 2), "iva": round(quota_iva, 2), "total": round(total_final, 2)
    }

def calcular_estadistiques_globals(llista_bars):
    print(">> Calculant mètriques de rendiment de la xarxa...")
    if not llista_bars:
        return None
    total_tapes = sum(b["tapes_venudes"] for b in llista_bars)
    preu_mig = sum(b["preu_tapa"] for b in llista_bars) / len(llista_bars)
    bar_top = max(llista_bars, key=lambda b: b["tapes_venudes"])
    return {
        "num_bars": len(llista_bars), "total_tapes": total_tapes,
        "preu_mitja": round(preu_mig, 2), "bar_popular": bar_top["nom"]
    }
