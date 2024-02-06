def converti_tempo(numero_secondi):
    # Calcolo anni
    anni = numero_secondi // (365 * 24 * 60 * 60)
    numero_secondi -= anni * (365 * 24 * 60 * 60)

    # Calcolo mesi
    mesi = numero_secondi // (30 * 24 * 60 * 60)
    numero_secondi -= mesi * (30 * 24 * 60 * 60)

    # Calcolo giorni
    giorni = numero_secondi // (24 * 60 * 60)
    numero_secondi -= giorni * (24 * 60 * 60)

    # Calcolo ore
    ore = numero_secondi // (60 * 60)
    numero_secondi -= ore * (60 * 60)

    # Calcolo minuti
    minuti = numero_secondi // 60
    numero_secondi -= minuti * 60

    # I secondi rimasti sono quelli che avanzano
    secondi = numero_secondi

    return anni, mesi, giorni, ore, minuti, secondi

# Prompt dell'input del numero di secondi
numero_secondi = int(input("Inserisci il numero di secondi: "))

# Chiamata alla funzione di conversione del tempo
anni, mesi, giorni, ore, minuti, secondi = converti_tempo(numero_secondi)

# Stampa del risultato
print(f"{anni} anni, {mesi} mesi, {giorni} giorni, {ore} ore, {minuti} minuti, {secondi} secondi")