def calcola_scatole_pasticcini(num_pasticcini):
    # Numero di scatole da 5 pezzi
    scatole_5 = num_pasticcini // 5
    num_pasticcini -= scatole_5 * 5
    
    # Numero di scatole da 3 pezzi
    scatole_3 = num_pasticcini // 3
    num_pasticcini -= scatole_3 * 3
    
    # Numero di scatole da 1 pezzo
    scatole_1 = num_pasticcini
    
    return scatole_5, scatole_3, scatole_1

# Esempio di utilizzo
numero_pasticcini = int(input("Inserisci il numero di pasticcini: "))
scatole_da_5, scatole_da_3, scatole_da_1 = calcola_scatole_pasticcini(numero_pasticcini)

print(f"Servono {scatole_da_5} scatole da 5 pezzi, {scatole_da_3} scatole da 3 pezzi e {scatole_da_1} scatole da 1 pezzo.")