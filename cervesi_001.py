# Richiedi il nome dell'alunno
nome_alunno = input("Inserisci il nome dell'alunno: ")

# Richiedi i voti dell'alunno
voto1 = float(input("Inserisci il primo voto: "))
voto2 = float(input("Inserisci il secondo voto: "))
voto3 = float(input("Inserisci il terzo voto: "))

# Calcola la media dei voti
media = (voto1 + voto2 + voto3) / 3

# Visualizza la media dei voti
print("La media dei voti di", nome_alunno, "è:", media)