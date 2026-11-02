def fattoriale(n):
    r = 1

    for i in range (1, n+1):
        r = r * i

    return r

n = int(input("inserisci un numero:"))

print("Il fattoriale è", fattoriale(n))