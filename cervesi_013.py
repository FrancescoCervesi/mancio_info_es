# Stampa la parola "ciao" 10 volte
for i in range(10):
    print("ciao")

# Somma dei numeri da 10 a 20
somma = 0
for i in range(10, 21):
    somma += i
print("La somma dei numeri da 10 a 20 è:", somma)

# Somma dei numeri pari fino a 30
somma_pari = 0
for i in range(1, 31):
    if i % 2 == 0:
        somma_pari += i
print("La somma dei numeri pari fino a 30 è:", somma_pari)

# Moltiplicazione dei numeri da 1 a 10
prod = 1
for i in range(1, 11):
    prod *= i
print("La moltiplicazione dei numeri da 1 a 10 è:", prod)