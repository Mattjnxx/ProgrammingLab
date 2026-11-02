def triangolo(a, b, c):
    if a+b<=c or a+c<=b or b+c<=a:
        return "Non possono foramre una triangolo"

    if a==b==c:
        return "Il triangolo è equilatero"
    elif a!=b!=c:
        return "Il trinagolo è scaleno"
    elif a==b or a==c or b==c:
        return "Il triangolo è isocele"

a = int(input("Inserisci un lato:"))
b = int(input("Inserisci un lato:"))
c = int(input("Inserisci un lato:"))

print(triangolo(a,b,c))