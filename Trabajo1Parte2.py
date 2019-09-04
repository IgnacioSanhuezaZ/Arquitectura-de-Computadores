""" Profesor: Juan Cubillos
    Asignaruta: Arquitectura de Computadores
    Alumnos: - Javier Gómes
             - Ignacio Sanhueza
Python 3.7
"""
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


def transformar(num):
    desde_hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    n = []
    for i in num:
        if not str(i).isdigit():
            n.append(desde_hex[i])
        else:
            n.append(int(i))
    return n


def suma(num1, num2, n):
    desde_hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    hacia_hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    acarreo = 0
    n1 = []
    n2 = []
    solucion = []
    n1 = transformar(num1)
    n2 = transformar(num2)
    n1.reverse()
    n2.reverse()
    for i in range(len(n1)):
        if acarreo != 0:
            n1[i] = n1[i] + acarreo
            acarreo = 0
        try:
            solucion.append((n1[i] + n2[i]) % n)
            acarreo = int((n1[i] + n2[i]) / n)
        except IndexError:
            while n1[i]:
                if acarreo != 0:
                    n1[i] = n1[i] + acarreo
                    acarreo = 0
                if n1[i] > n:
                    n1[i] = n1[i] % n
                    acarreo = int(n1[i] / n)
                solucion.append(n1[i])
            break
    i = len(n1)
    if len(n2) > len(n1):
        while i < len(n2):
            if acarreo != 0:
                n2[i] = + acarreo
                acarreo = 0
            if n2[i] > n:
                n2[i] = n2[i] % n
                acarreo = int(n2[i] / n)
            solucion.append(n2[i])
            i += 1
    if acarreo != 0:
        solucion.append(acarreo)
    sol = ""
    solucion.reverse()
    for i in solucion:
        if i > 9:
            i = hacia_hex[i]
        sol = sol + str(i)
    return sol


def comparar(n1, n2):
    if len(n1) < len(n2):
        return -1
    elif len(n1) == len(n2):
        for i in range(len(n1)):
            if n1[i] < n2[i]:
                return 1
            elif n1[i] > n2[i]:
                return -1
        return 0
    else:
        return 1


def resta(num1, num2, n):
    desde_hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    hacia_hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    acarreo = 0
    solucion = []
    signo = False
    n1 = transformar(num1)
    n1.reverse()
    n2 = transformar(num2)
    n2.reverse()
    if comparar(n1, n2) < 0:
        signo = True
        for i in range(len(n1)):
            if acarreo != 0:
                n2[i] -= acarreo
                acarreo = 0
            if n2[i] - n1[i] < 0:
                solucion.append(n2[i] + 16 - n1[i])
                acarreo += 1
            else:
                solucion.append(n2[i] - n1[i])
        if len(n2) != len(n1):
            i = len(n1)
            while i < len(n2):
                if acarreo != 0:
                    n2[i] = n2[i] - acarreo
                    acarreo = 0
                if n2[i] > n:
                    n2[i] = n2[i] % n
                    acarreo = int(n2[i] / n)
                solucion.append(n2[i])
                i += 1
    elif comparar(n1, n2) > 0:
        for i in range(len(n2)):
            if acarreo != 0:
                n1[i] -= acarreo
                acarreo = 0
            if n1[i] - n2[i] < 0:
                solucion.append(n1[i] + 16 - n2[i])
                acarreo += 1
            else:
                solucion.append(n1[i] - n2[i])
        if len(n1) != len(n2):
            i = len(n2)
            while i < len(n1):
                if acarreo != 0:
                    n1[i] = n1[i] - acarreo
                    acarreo = 0
                if n1[i] > n:
                    n1[i] = n1[i] % n
                    acarreo = int(n1[i] / n)
                solucion.append(n1[i])
                i += 1
    else:
        return "0"
    sol = ""
    solucion.reverse()
    for i in solucion:
        if i > 9:
            i = hacia_hex[i]
        sol = sol + str(i)
    if signo == True:
        sol = "-" + sol
    return sol

print("Primer trabajo de Arquitectura de Computadores: Parte 2")
print("Programa que suma o resta dos numeros hexdecimales\n")

op = int(input("1- sumar dos numeros hexadecimales\n2- restar dos numeros hexadecimales (el primero menos el segundo)\nIngrese la opcion a realizar: "))
while op != 1 and op != 2:
    op = input("La opcion ingresada no es valida, ingrese la opcion 1 o 2 : ")
    if op != 10 and op != 16:
        break
num1 = verificar_hex(input("Ingrese el primer numero: "))
num2 = verificar_hex(input("Ingrese el segundo numero: "))
if op == 1:
    print(num1 + "\n" + num2 + "\n+ --------------------------\n" + suma(num1,num2, 16))
elif op == 2:
    print(num1 + "\n" + num2 + "\n- --------------------------\n" + resta(num1,num2, 16))
else:
    print("Error de opcion: escoja una opcion valida")
