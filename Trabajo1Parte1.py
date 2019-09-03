def dec_to_r(num, n):
    hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    aux1 = num
    solucion = []
    while aux1:
        solucion.append(int(aux1 % n))
        aux1 = int(aux1 / n)
    aux2 = ""
    solucion.reverse()
    for i in solucion:
        if i > 9:
            i = hex[i]
        aux2 = aux2 + str(i)
    return aux2


def hex_to_bin(num):
    hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    aux = 0
    solucion = []
    le = len(num) - 1
    for i in num:
        if not i.isdigit():
            aux = dec_to_r(int(hex[i]), 2)
            while len(aux) < 4:
                aux = "0" + aux
            solucion.append(aux)
        else:
            aux = dec_to_r(int(i), 2)
            while len(aux) < 4:
                aux = "0" + aux
            solucion.append(aux)
    aux = ""
    for i in solucion:
        aux = aux + i
    return aux


def hex_to_dec(num):
    aux = len(num) - 1
    hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    solucion = []
    for i in num:
        if not str(i).isdigit():
            i = hex[i]
        s = 16 ** aux
        s = s * int(i)
        solucion.append(s)
        aux -= 1
    aux2 = 0
    for i in solucion:
        aux2 += i
    return aux2


def hex_to_hect(num):
    return dec_to_r(hex_to_dec(num), 8)


def verificar_hex(num):
    letras = ["A", "B", "C", "D", "E", "F"]
    for i in num:
        if i.isdigit() == False or (int(i) < 0 and (int(i) > 9)):
            if i not in letras:
                nu = input(
                    "El numero ingresado no es en base 16, ingrese uno nuevamente (recuerde que las letras usadas son "
                    "siempre en mayusculas): ")
                nu = verificar_hex(nu)
                return nu
    return num


def verificar_dec(num):
    for i in num:
        if not i.isdigit():
            nu = input("El numero ingresado no es en base 10, ingrese uno nuevamente: ")
            nu = verificar_dec(nu)
            return nu
    return num

print("Primer trabajo de Arquitectura de Computadores: Parte 1")
print("Programa que transofrma numeros de base decimal o hexadecimal a binario, octal y a decimal (siendo hexadecimal) o hexadecimal (siendo decimal)\n")
op = int(input("Ingrese la base del numero a ingresar (10,16) : "))
while op != 10 and op != 16:
    op = input("La opcion ingresada no es valida, ingrese una base 10 o 16 (10,16) : ")
    if op != 10 and op != 16:
        break
num = input("Ingrese el numero: ")
if op == 10:
    num = verificar_dec(num)
    print("El numero ingresado en base binaria: ")
    print(dec_to_r(int(num), 2))
    print("El numero ingresado en base octal: ")
    print(dec_to_r(int(num), 8))
    print("El numero ingresado en base hexadecimal: ")
    print(dec_to_r(int(num), 16))
else:
    num = verificar_hex(num)
    print("El numero ingresado en base decimal: ")
    print(hex_to_dec(num))
    print("El numero ingresado en base binaria: ")
    print(hex_to_bin(num))
    print("El numero ingresado en base octal: ")
    print(hex_to_hect(num))
