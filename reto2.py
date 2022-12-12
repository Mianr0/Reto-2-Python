i = 1
cont = int(input())
cont_aceptados = 0
cont_sre = 0
cont_afr = 0
cont_ind = 0
cont_rai = 0
cont_pal = 0
cont_git = 0

while(i <= cont):
    reconocimiento_etnico = (input())
    estrato_socioeconomico = int(input())
    ingresos_del_nucleo_familiar = int(input())
    puntaje = float (0)

    if (reconocimiento_etnico != "sin reconocimiento" and reconocimiento_etnico != "afrodescendiente" and reconocimiento_etnico != "indigena" and reconocimiento_etnico != "raizal" and reconocimiento_etnico != "palenquero" and reconocimiento_etnico != "gitano"):
        i += 1
        continue

    else:
        if (estrato_socioeconomico != (1) and estrato_socioeconomico != (2) and estrato_socioeconomico != (3) and estrato_socioeconomico != (4) and estrato_socioeconomico != (5) and estrato_socioeconomico != (6)):
            i += 1
            continue

        else:

            i += 1

            if (reconocimiento_etnico == "sin reconocimiento"):
                puntaje = (puntaje + 0)
                cont_sre += 1

            if (reconocimiento_etnico == "afrodescendiente"):
                puntaje = (puntaje + 9)
                cont_afr += 1

            if (reconocimiento_etnico == "indigena"):
                puntaje = (puntaje + 10)
                cont_ind += 1

            if (reconocimiento_etnico == "raizal"):
                puntaje = (puntaje + 11)
                cont_rai += 1

            if (reconocimiento_etnico == "palenquero"):
                puntaje = (puntaje + 12)
                cont_pal += 1

            if (reconocimiento_etnico == "gitano"):
                puntaje = (puntaje + 13)
                cont_git += 1

            if (estrato_socioeconomico == 1):
                puntaje = (puntaje + 15)

            if (estrato_socioeconomico == 2):
                puntaje = (puntaje + 13)

            if (estrato_socioeconomico == 3):
                puntaje = (puntaje + 11)

            if (estrato_socioeconomico == 4):
                puntaje = (puntaje + 7)

            if (estrato_socioeconomico == 5):
                puntaje = (puntaje + 0)

            if (estrato_socioeconomico == 6):
                puntaje = (puntaje + 0)

            if (ingresos_del_nucleo_familiar < 908526):
                puntaje = (puntaje + 20)

            if (ingresos_del_nucleo_familiar >= 908526 and ingresos_del_nucleo_familiar < 1817052):
                puntaje = (puntaje + 14)

            if (ingresos_del_nucleo_familiar >= 1817052 and ingresos_del_nucleo_familiar < 3634104):
                puntaje = (puntaje + 12)

            if (ingresos_del_nucleo_familiar >= 3634104 and ingresos_del_nucleo_familiar < 4542630):
                puntaje = (puntaje + 9)

            if (ingresos_del_nucleo_familiar >= 4542630):
                puntaje = (puntaje + 0)

            if (puntaje >= 30):
                cont_aceptados += 1

print(cont_aceptados)
print("sin reconocimiento ", cont_sre)
print("afrodescendiente ", cont_afr)
print("indigena ", cont_ind)
print("raizal ", cont_rai)
print("palenquero ", cont_pal)
print("gitano ", cont_git)