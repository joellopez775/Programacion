import datetime

propiedades = []

def grabar_propiedad():
    print("╔══════════════════════════╗")
    print("║       Grabar Propiedad   ║")
    print("╚══════════════════════════╝")
    codigo = input("Ingrese el código de la propiedad: ")
    tipo = input("Ingrese el tipo de la propiedad (ARRIENDO/VENTA): ")
    comuna = input("Ingrese la comuna de la propiedad: ")
    
    fecha_valida = False
    while not fecha_valida:
        fecha_publicacion = input("Ingrese la fecha de publicación (DD/MM/AAAA): ")
        try:
            fecha_publicacion = datetime.datetime.strptime(fecha_publicacion, "%d/%m/%Y")
            fecha_valida = True
        except ValueError:
            print("Fecha inválida. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")
    
    valor = float(input("Ingrese el valor de la propiedad: "))
    moneda = input("Ingrese la moneda (UF/CLP): ")
    
    propiedad = {
        "codigo": codigo,
        "tipo": tipo,
        "comuna": comuna,
        "fecha_publicacion": fecha_publicacion,
        "valor": valor,
        "moneda": moneda
    }
    
    propiedades.append(propiedad)
    print("Propiedad grabada exitosamente.")

def buscar_propiedad():
    print("╔══════════════════════════╗")
    print("║        Buscar Propiedad  ║")
    print("╚══════════════════════════╝")
    codigo = input("Ingrese el código de la propiedad a buscar: ")
    encontrada = False
    
    for propiedad in propiedades:
        if propiedad["codigo"] == codigo:
            print("Propiedad encontrada:")
            print("Código:", propiedad["codigo"])
            print("Tipo:", propiedad["tipo"])
            print("Comuna:", propiedad["comuna"])
            print("Fecha de publicación:", propiedad["fecha_publicacion"].strftime("%d/%m/%Y"))
            print("Valor:", propiedad["valor"])
            print("Moneda:", propiedad["moneda"])
            encontrada = True
            break
    
    if not encontrada:
        print("No se encontró ninguna propiedad con el código", codigo)

def imprimir_propiedades():
    print("╔══════════════════════════╗")
    print("║    Imprimir Propiedades  ║")
    print("╚══════════════════════════╝")
    print("Propiedades registradas:")
    
    for propiedad in propiedades:
        print("Código:", propiedad["codigo"])
        print("Tipo:", propiedad["tipo"])
        print("Comuna:", propiedad["comuna"])
        print("Fecha de publicación:", propiedad["fecha_publicacion"].strftime("%d/%m/%Y"))
        print("Valor:", propiedad["valor"])
        print("Moneda:", propiedad["moneda"])
        print("-----")
    
    if not propiedades:
        print("No hay propiedades registradas.")

def main():
    while True:
        print("╔══════════════════════════╗")
        print("║            MENÚ          ║")
        print("╚══════════════════════════╝")
        print("1) Grabar Propiedad")
        print("2) Buscar Propiedad")
        print("3) Imprimir Propiedades")
        print("4) Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            grabar_propiedad()
        elif opcion == "2":
            buscar_propiedad()
        elif opcion == "3":
            imprimir_propiedades()
        elif opcion == "4":
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
