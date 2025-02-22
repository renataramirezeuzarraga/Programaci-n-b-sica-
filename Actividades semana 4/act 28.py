#28. Simular una cuenta bancaria con dep´ositos y retiros.

saldo = 100  

while True:
    print("\n*** Menú de la cuenta bancaria ***")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Ver saldo")
    print("4. Salir")
    
    opcion = input("Opción: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso: {monto} unidades. Saldo actual: {saldo}")
        else:
            print("El monto del depósito debe ser mayor que cero.")
    
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f"Retiro exitoso: {monto} unidades. Saldo actual: {saldo}")
            else:
                print("Fondos insuficientes para el retiro.")
        else:
            print("El monto del retiro debe ser mayor que cero.")
    
    elif opcion == "3":
        print(f"Saldo actual: {saldo}")
    
    elif opcion == '4':
        print("Gracias por usar el sistema")
        break
    
    else:
        print("Opción no válida, por favor intente nuevamente")
