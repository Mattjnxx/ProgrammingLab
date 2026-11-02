def conta_vocali(frase):
    vocali = "aeiou"
    contatore = 0

    for carattere in frase.lower():
        if carattere in vocali:
            contatore+=1

    return contatore

frase = input("Inserisci una frase: ")

print("La frase ha", conta_vocali(frase), "vocali")