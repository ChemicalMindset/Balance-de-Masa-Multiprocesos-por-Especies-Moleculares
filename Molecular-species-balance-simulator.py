# Simulación multiprocesos para balance de masa por especies moleculares en un reactor químico

#Librerias
import matplotlib.pyplot as plt
import numpy as np

def fosforo_blanco():

    Mr_fosfato_tricalcico = 310.18
    Mr_dioxido_silicio = 60.08
    Mr_coque = 12.01
    Mr_fosforo_blanco = 123.88
    Mr_silicato_calcio = 116.16
    Mr_monoxido_carbono = 28.01

    print("\nEl fosforo blanco se obtiene a partir del tratamiento de fosforo tricalcico con cantidad estequimetrica de arena y exceso de coque a altas temperaturas segun:",
          "\n2 Ca3(PO4)2 + 6 SiO2 + 10 C → P4 + 6 CaSiO3 + 10 CO",
          "\nRendimiento del 80%")

    masa_fosfato_tricalcico_A = float(input("Ingrese la masa de fosfato tricalcico (kilogramos/hora) de alimentación: "))
    rendimiento_1 = 0.80
    exceso_coque = 0.50

    print("\nCorriente masica de reactivos de alimentación del reactor (A)")
    print("Masa de fosfato tricalcico:", masa_fosfato_tricalcico_A, "kg/h")
    print("Rendimiento de la reacción:", rendimiento_1 * 100, "%")
    print("Factor de reactivo en exceso:", exceso_coque * 100, "%")

    print("\nCorriente masica de salida del reactor (G)")
    masa_fosforo_blanco_G = masa_fosfato_tricalcico_A * (Mr_fosforo_blanco / (2 * Mr_fosfato_tricalcico)) * rendimiento_1
    masa_monoxido_carbono_G = masa_fosfato_tricalcico_A * (10 * Mr_monoxido_carbono / (2 * Mr_fosfato_tricalcico)) * rendimiento_1
    masa_silicato_calcio_G = 0

    print("Masa de fosforo blanco de saluda es:", masa_fosforo_blanco_G, "kg/h")
    print("Masa de monóxido de carbono de salida es:", masa_monoxido_carbono_G, "kg/h")
    print("Masa de silicato de calcio de salida es:", masa_silicato_calcio_G, "kg/h")

    G = masa_fosforo_blanco_G + masa_monoxido_carbono_G + masa_silicato_calcio_G
    print("Masa total de los productos que salen del reactor:", G, "kg/h")

    print("\nCorriente masica de escoria del reactor (E)")
    masa_fosforo_blanco_E = 0
    masa_monoxido_carbono_E = 0
    masa_silicato_calcio_E = masa_fosfato_tricalcico_A * (6 * Mr_silicato_calcio / (2 * Mr_fosfato_tricalcico)) * rendimiento_1

    print("Masa de fosforo blanco de escoria es:", masa_fosforo_blanco_E, "kg/h")
    print("Masa de monóxido de carbono de escoria es:", masa_monoxido_carbono_E, "kg/h")
    print("Masa de silicato de calcio de escoria es:", masa_silicato_calcio_E, "kg/h")







def plata_metalica():
    print("\nLa plata metalica puede obtenerse por tratamiento de sulfato de plata con cobre.",
          "\n Cu + Ag2SO4 → CuSO4 + 2 Ag")
    masa_cobre = float(input("Ingrese la masa de cobre (kilogramos/hora): "))
    masa_sulfato_plata = float(input("Ingrese la masa de sulfato de plata (kilogramos/hora): "))

    print("Masa de cobre es:", masa_cobre)
    print("Masa de sulfato de plata es:", masa_sulfato_plata)





    # Menú principal del Sistema
def main():

    while True:

        print(f"=" * 20,
              f" SISTEMA DE SIMULACIÓN DE BALANCE DE MASA POR ESPECIES MOLECULARES ",
              f"=" * 20)
        print("Seleccione la reaccion quimica que desea simular:")

        print("1. Sintesis termica de fosforo blanco.")
        print("2. Extracción de plata por Redox.")

        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            fosforo_blanco()

        elif opcion == "2":
            plata_metalica()

        elif opcion == "0":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción incorrecta.")

# Programa principal
if __name__ == "__main__":
    main()