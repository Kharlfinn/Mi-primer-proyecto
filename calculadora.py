import time

def menu_calculadora():
    print("""\n*** Opciones calculadora ***

    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir""")
    while True:
        try:
            opcion = int(input("\nElige una opción: "))
            if opcion in [1,2,3,4,5]:
                return opcion
            else:
                print("Opción inválida. Re-intente.")
        except ValueError:
            print("Opción inválida. Re-intente.")

def solicitar_numeros():
    while True:
        try:
            op1 = float(input("Ingresa el primer número: "))
            op2 = float(input("Ingresa el segundo número: "))
            return op1,op2
        except ValueError:
            print("Opción inválida. Re-intente.")

def sumar():
    num1,num2 = solicitar_numeros()
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
    time.sleep(2)

def restar():
    num1,num2 = solicitar_numeros()
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es: {resultado}")
    time.sleep(2)

def multiplicar():
    num1,num2 = solicitar_numeros()
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    time.sleep(2)

def dividir():
    while True:    
        num1,num2 = solicitar_numeros()
        try:
            resultado = num1/num2
            print(f"La división de {num1} y {num2} es {resultado}")
            break
        except ZeroDivisionError:
            print("¡No puedes dividir en 0!")
    time.sleep(2)

def exit():
    print("¡Gracias por usar la calculadora!")
    salir = True
    return salir
    
def calculadora():
    salir = False
    while not salir:
        opcion = menu_calculadora()
        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()
        elif opcion == 5:
            salir = exit()

calculadora()

