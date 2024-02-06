def calcola_media_ponderata(voto1, crediti1, voto2, crediti2, voto3, crediti3):
    if voto1 < 1 or voto1 > 30 or crediti1 < 1 or crediti1 > 12:
        print("Voto o crediti non validi per il primo esame")
        return
    if voto2 < 1 or voto2 > 30 or crediti2 < 1 or crediti2 > 12:
        print("Voto o crediti non validi per il secondo esame")
        return
    if voto3 < 1 or voto3 > 30 or crediti3 < 1 or crediti3 > 12:
        print("Voto o crediti non validi per il terzo esame")
        return
    
    peso1 = voto1 * crediti1
    peso2 = voto2 * crediti2
    peso3 = voto3 * crediti3
    
    somma_pesata = peso1 + peso2 + peso3
    somma_crediti = crediti1 + crediti2 + crediti3
    
    media_ponderata = somma_pesata / somma_crediti
    
    return media_ponderata

# Esempio di utilizzo
voto1 = int(input("Inserisci il voto in trentesimi del primo esame: "))
crediti1 = int(input("Inserisci il numero di crediti del primo esame: "))
voto2 = int(input("Inserisci il voto in trentesimi del secondo esame: "))
crediti2 = int(input("Inserisci il numero di crediti del secondo esame: "))
voto3 = int(input("Inserisci il voto in trentesimi del terzo esame: "))
crediti3 = int(input("Inserisci il numero di crediti del terzo esame: "))

media = calcola_media_ponderata(voto1, crediti1, voto2, crediti2, voto3, crediti3)
if media:
    print("La media ponderata dei voti è:", media)