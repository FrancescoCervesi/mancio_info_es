#In una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effettuare secondo la seguente tabella:
#n.1-19 0,10 euro, n.20-100 0,08 euro, piu di 100 0,05 euro. 
#Inoltre se le fotocopie sono da rilegare viene aggiunto un costo di 1,80 euro.
#Dati in input il numero di fotocopie da effettuare, il nome del cliente e un indicazione che segnali se il plico è da rilegare, calcola il costo totale e stampa il seguente prospetto:
#Gentile Sig. ___ il suo preventivo è di ___ euro compresa la rilegatura. L'ultima riga è da scrivere solo se è richiesta la rilegatura
num_fotocopie = int(input("numero di fotocopie da effettuare: "))
nome_cliente = (input("nome del cliente: "))
rilegatura = (input("il plico è da rilegare? (si/no): "))

if num_fotocopie >= 1 and num_fotocopie <= 19:
    costo_unitario = 0.10
elif num_fotocopie >= 20 and num_fotocopie <= 100:
    costo_unitario = 0.08 
else:
    costo_unitario = 0.05 
     
costo_totale = costo_unitario * num_fotocopie

if rilegatura == "si":
    costo_totale += 1.80
    print(f"gentile sig.{nome_cliente} il suo preventivo è {costo_totale} euro compresa la rilegatura.")
elif rilegatura == "no":
    print(f"gentile sig.{nome_cliente} il suo preventivo è {costo_totale} euro.")
    






