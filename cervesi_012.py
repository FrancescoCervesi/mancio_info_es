n = int(input("Quanti valori vuoi inserire? "))
somma = 0

for i in range(n):
    valore = float(input("Inserisci il valore: "))
    somma += valore

print("La somma dei valori inseriti è:", somma)