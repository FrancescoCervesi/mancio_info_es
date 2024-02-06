# Input dei tre numeri
n1 = float(input("Inserisci il primo numero: "))
n2 = float(input("Inserisci il secondo numero: "))
n3 = float(input("Inserisci il terzo numero: "))

# Trovare il maggiore tra i tre numeri
if n1 > n2 and n1 > n3:
    maggiore = n1
elif n2 > n1 and n2 > n3:
    maggiore = n2
else:
    maggiore = n3

# Mostrare il risultato
print("Il numero maggiore è:", maggiore)