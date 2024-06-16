import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    usuario_gana = 0
    computadora_gana = 0

    while True:
        print("\nElige una opción: ")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("4. Salir")

        eleccion_usuario = input("Tu elección: ")

        if eleccion_usuario == '4':
            print(f"\nResultados finales: Usuario {usuario_gana} - Computadora {computadora_gana}")
            print("Gracias por jugar. ¡Adiós!")
            break

        if eleccion_usuario not in ['1', '2', '3']:
            print("Elección no válida, por favor elige nuevamente.")
            continue

        eleccion_usuario = int(eleccion_usuario) - 1
        eleccion_computadora = random.choice(opciones)

        print(f"Usuario elige: {opciones[eleccion_usuario]}")
        print(f"Computadora elige: {eleccion_computadora}")

        if opciones[eleccion_usuario] == eleccion_computadora:
            print("Es un empate!")
        elif (opciones[eleccion_usuario] == 'piedra' and eleccion_computadora == 'tijera') or \
             (opciones[eleccion_usuario] == 'papel' and eleccion_computadora == 'piedra') or \
             (opciones[eleccion_usuario] == 'tijera' and eleccion_computadora == 'papel'):
            print("¡Ganas tú!")
            usuario_gana += 1
        else:
            print("¡Gana la computadora!")
            computadora_gana += 1

if __name__ == "__main__":
    jugar()
       

       

