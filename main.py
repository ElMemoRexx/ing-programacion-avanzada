from sumar import sumar
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada


def menu():
    while True:
        print("\n=== CALCULADORA ===")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Suma avanzada (N números)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", sumar(a, b))

        elif opcion == "2":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", restar(a, b))

        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", multiplicar(a, b))

        elif opcion == "4":
            a = float(input("Dividendo: "))
            b = float(input("Divisor: "))
            print("Resultado:", dividir(a, b))

        elif opcion == "5":
            n = int(input("¿Cuántos números vas a sumar? "))
            numeros = []
            for i in range(n):
                numero = float(input(f"Número {i + 1}: "))
                numeros.append(numero)
            print("Resultado:", suma_avanzada(numeros))

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
