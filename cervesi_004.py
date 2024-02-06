# Chiedi all'utente il numero di adulti nel gruppo
num_adulti = int(input("Inserisci il numero di adulti nel gruppo: "))

# Chiedi all'utente il numero di minori nel gruppo
num_minorenni = int(input("Inserisci il numero di minori nel gruppo: "))

# Calcola la spesa complessiva
spesa_adulti = num_adulti * 10
spesa_minorenni = num_minorenni * 6
spesa_complessiva = spesa_adulti + spesa_minorenni

# Stampa la spesa complessiva
print("La spesa complessiva per il gruppo è di", spesa_complessiva, "euro.")