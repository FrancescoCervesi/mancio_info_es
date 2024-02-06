# Definizione dei costi giornalieri dei servizi
costo_ombrellone = 12
costo_lettini = 5
costo_sdraio = 6.50

# Richiesta in input del numero di giorni e dei servizi prenotati
numero_giorni = int(input("Inserisci il numero di giorni: "))
numero_ombrelloni = int(input("Inserisci il numero di ombrelloni: "))
numero_lettini = int(input("Inserisci il numero di lettini: "))
numero_sdraio = int(input("Inserisci il numero di sedie a sdraio: "))

# Calcolo della spesa complessiva
spesa_ombrelloni = costo_ombrellone * numero_giorni * numero_ombrelloni
spesa_lettini = costo_lettini * numero_giorni * numero_lettini
spesa_sdraio = costo_sdraio * numero_giorni * numero_sdraio
spesa_complessiva = spesa_ombrelloni + spesa_lettini + spesa_sdraio

# Stampa della spesa complessiva
print("La spesa complessiva è di", spesa_complessiva, "euro.")