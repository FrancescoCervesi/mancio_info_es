#crivere un programma che passati in input un numero non definito a priori di voti, ne calcoli la media.
#Il programma terminerà con l'iterazione degli input quando inseriamo un valore <=0.
#Non si  considerino ai fini della media, i voti >10.



num_voti = 0
somma = 0

i = 1
while  i > 0:
    voto = float(input("inserisci un voto: "))
    if voto > 10:
        num_voti += 0
    elif voto <= 0:
        i = 0
    else:
        num_voti += 1
        somma += voto

        media = somma / num_voti
        print(f"la media è:  {media}")