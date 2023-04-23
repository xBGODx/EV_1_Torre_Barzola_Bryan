a = int(input("ingrese un numero: "))
b = int(input("ingrese otro numero: "))

c = a // b
r = a % b

if a >= b:
    print("nose puede imprimir la serie")
else:
    while a <= b:
        print(a)
        a += 5