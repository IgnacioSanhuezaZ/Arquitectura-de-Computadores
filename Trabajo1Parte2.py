from Trabajo1Parte1 import hex_to_dec, validar_hex

def suma(num1, num2):
    desde_hex = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    hacia_hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    acarreo = 0
    n1 = []
    n2 = []
    for i in num1:
        if not str(i).isdigit():
            n1.append(desde_hex[i])
        else:
            n1.append(int(i))
    for i in num2:
        if not str(i).isdigit():
            n2.append(desde_hex[i])
        else:
            n2.append(int(i))
    n1 = n1.reverse()
    n2 = n2.reverse()
