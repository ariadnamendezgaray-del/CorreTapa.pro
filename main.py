import config
import logica
import interface

def gestionar_aplicacio():
 mostrar_benvinguda()
    actiu = True
    while actiu:
        mostrar_menu_principal()
        opcio = demanar_opcio()
        if opcio == "1":
            mostrar_carta_bars(obtenir_tots_els_bars())
        elif opcio == "2":
            zona = demanar_zona_cerca()
            trobats = filtrar_bars_per_zona(zona)
            if trobats:
                mostrar_carta_bars(trobats)
            else:
                print(f"❌ No s'ha trobat cap bar a '{zona}'.")
        elif opcio == "3":
            reserva = demanar_dades_reserva()
            if reserva:
                bar = cercar_bar_per_id(reserva["id_bar"])
                if not bar:
                    print("❌ No existeix aquest bar.")
                elif not validar_disponibilitat(bar["aforament_actual"], reserva["persones"], bar["aforament_max"]):
                    print(MSG_ERROR_AFORAMENT)
                else:
                    detall = calcular_total_comanda(bar["preu_tapa"], reserva["tapes"], reserva["persones"], reserva["es_soci"])
                    actualitzar_dades_bar(bar["id"], reserva["persones"], reserva["tapes"])
                    mostrar_resum_comanda(bar, reserva, detall)
        elif opcio == "4":
            stats = calcular_estadistiques_globals(obtenir_tots_els_bars())
            mostrar_panell_estadistiques(stats)
        elif opcio == "0":
            print(f"\nGràcies per utilitzar {NOM_ESDEVENIMENT}. Fins aviat!")
            actiu = False
        else:
            print(MSG_OPCIO_INVALIDA)

if __name__ == "__main__":
    gestionar_aplicacio()