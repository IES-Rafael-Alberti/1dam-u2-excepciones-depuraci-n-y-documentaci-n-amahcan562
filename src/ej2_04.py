def pedirNumero():
    salir = False
    while not salir:
        numero_str = input("Introduzca un número entero: ")

        try:
            int(numero_str)
            salir = True
        except ValueError:
            print("La entrada no es correcta.")
        except Exception:
            print("ERROR")


def main():
    pedirNumero()


if __name__ == "__main__":
    main()