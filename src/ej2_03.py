def pedirNumero():
    salir = False
    while not salir:
        numero_str = input("Introduzca un número entero positivo: ")

        try:
            numero = int(numero_str)
            if numero > 0:
                salir = True
            else:
                print("Introduzca un número positivo:")
        except ValueError:
            print("Número no válido.")
        except Exception:
            print("ERROR")
    return numero

def cuentaAtras(numero):
    for i in range (numero, 0, -1):
        if i == 1:
            print("1, 0")
        else:
            print(i, end=", ")

def main():
    numero = pedirNumero()

    cuentaAtras(numero)

if __name__ == "__main__":
    main()