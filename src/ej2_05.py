def pedirContraseña():
    contraseña = input("Introduzca la contraseña: ")

    if contraseña != "hola":
        raise NameError

    

def main():
    salir = False
    while not salir:
        try:
            pedirContraseña()
            salir = True
        except NameError:
            print("Incorrect Password!!")

    print("Lo has conseguido!")

if __name__ == "__main__":
    main()