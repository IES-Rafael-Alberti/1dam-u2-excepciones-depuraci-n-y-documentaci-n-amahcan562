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

def impares(numero):
    i = 1
    while i <= numero:
        print(i, end="")
        if i < numero - 1 and i % 2 != 0:
            print(", ", end="")
        i += 2


def main():

    numero = pedirNumero()

    impares(numero)

if __name__ == "__main__":
    main()