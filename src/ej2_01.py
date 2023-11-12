def vida(edad):
    n = 1
    while n <= int(edad):
        print(n, end=" ")
        n += 1

def pedirEdad():
    salir = False
    while not salir:
        edad_str = input("Introduzca su edad: ")

        try:
            edad = int(edad_str)
            salir = True
        except ValueError:
            print("Edad no válida")
        except Exception:
            print("Error")

def main():

    edad = pedirEdad()

    vida(edad)

if __name__ == "__main__":
    main()