n = int(input("Inserisci un numero: "))

primo = True

for i in range(2, n):
    if n % 1 == 0:
        primo = False

if n < 2:
    primo = False

if primo:
    print("è primo")
else:
    print("non è primo")
