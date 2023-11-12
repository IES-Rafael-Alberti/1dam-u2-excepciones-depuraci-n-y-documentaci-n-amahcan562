def pedirContraseña():
    salir = False
    while not salir:
        contraseña = input("Introduzca la contraseña: ")

        try:
            contraseña == "vivaespaña"
            salir = True
        except NameError:
            print("Incorrect Password!!")
    return contraseña

def main():
    pedirContraseña()

if __name__ == "__main__":
    main()