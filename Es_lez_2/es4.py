def conta_lettera(parola, lettera):
    return parola.count(lettera)

parola = input("Inserisci una parola: ")
lettera = input("Inserisci una lettera: ")

r = conta_lettera(parola, lettera)
print("La lettera è contenuta", r, "volte")