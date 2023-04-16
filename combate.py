import random
import time
import os
from playsound import playsound
from clase import Clase
from character import Character


def simulaBatalla(warrior1, warrior2):
    time.sleep(2)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.4)
        os.system('cls' if os.name == 'nt' else 'clear')
        playsound(f"sound/{i}.mp3")
    print("¡¡¡ FIGHT !!!")
    time.sleep(0.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    playsound("sound/stage.mp3", False)
    playsound("sound/lucha.mp3")

    # Determino qué guerrero tiene la mayor velocidad para que empiece primero
    if warrior1.speed > warrior2.speed:
        golpeador = warrior1
        receptor = warrior2
    elif warrior1.speed < warrior2.speed:
        golpeador = warrior2
        receptor = warrior1
    else:
        # Si tienen la misma velocidad, determino aleatoriamente quién empieza
        if random.choice([True, False]):
            golpeador, receptor = warrior1, warrior2
        else:
            golpeador, receptor = warrior2, warrior1

    golpeExtra = 0
    limite = 50
    # Empieza la pelea
    while warrior1.stayAlive() and warrior2.stayAlive():
        golpeador.hit(receptor)
        golpeExtra += warrior1.speed
        if golpeExtra >= limite:
            print("Ataque extra!")
            golpeador.hit(receptor)
            golpeExtra -= 50
        golpeador, receptor = receptor, golpeador

    # Muestro el resultado de la pelea
    if warrior1.life <= 0:
        print(f"{warrior2.name} ES EL GANADOR!! 🏆")
        playsound("sound/you.mp3")
        playsound("sound/win.mp3")
        time.sleep(1)
    elif warrior2.life <= 0:
        print(f"{warrior1.name} ES EL GANADOR!! 🏆")
        playsound("sound/you.mp3")
        playsound("sound/win.mp3")
        experience = (warrior2.level * 10)/2
        warrior1.ganar_combate(experience)
        print(f"{warrior1.name} ha ganado {warrior1.experience}/{warrior1.next_level} más para alcanzar el siguiente nivel.")
        time.sleep(1)

continuar = True
personaje1 = None
personaje2 = None

while continuar:
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(2):
        if i == 0:
            print("🥋 PRIMER PARTICIPANTE 🥊")
            name1 = input("Ingresa el nombre de tu personaje: ")
            name = name1
        else:
            print("🥋 SEGUNDO PARTICIPANTE 🥊")
            name2 = input("Ingresa el nombre de tu personaje: ")
            name = name2
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"-----| {name} |-----")
        print("Selecciona la clase de tu personaje: ")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Picaro")
        clase_elegida = int(input("Ingresa el número de la clase elegida: "))

        if clase_elegida == 1:
            clase = Clase("Guerrero",20, 7, 3, 3, 4)
        elif clase_elegida == 2:
            clase = Clase("Mago",15, 5, 8, 4, 2)
        elif clase_elegida == 3:
            clase = Clase("Pícaro",10, 4, 6, 6, 2)
        else:
            print("Selección inválida")

        os.system('cls' if os.name == 'nt' else 'clear')

        atributos_disponibles = {
            1: 'vida',
            2: 'fuerza',
            3: 'precision',
            4: 'velocidad',
            5: 'defensa'
        }

        puntos_disponibles = 15
        atributos_elegidos = {}

        while puntos_disponibles > 0:
            print(f"-----| {name} |-----")
            print(f'Tienes {puntos_disponibles} puntos para asignar')
            print('Atributos disponibles:')
            for k, v in atributos_disponibles.items():
                print(f'{k}. {v}')
            atributo_elegido = int(input('Elige un atributo (introduce el número correspondiente): '))
            if atributo_elegido not in atributos_disponibles:
                print('Opción no válida, vuelve a intentarlo')
                continue
            puntos_a_asignar = int(input('¿Cuántos puntos quieres asignar a este atributo?: '))
            if puntos_a_asignar > puntos_disponibles:
                print(f'Sólo tienes {puntos_disponibles} puntos disponibles')
                continue
            os.system('cls' if os.name == 'nt' else 'clear')
            atributo_actual = atributos_disponibles[atributo_elegido]
            atributos_elegidos[atributo_actual] = puntos_a_asignar
            puntos_disponibles -= puntos_a_asignar

        print('\nAtributos elegidos:')
        for k, v in atributos_elegidos.items():
            print(f'{k.capitalize()}: {v}')

        personaje = Character(clase,
                            name1 if i == 0 else name2,
                            atributos_elegidos.get('vida', 0),
                            atributos_elegidos.get('fuerza', 0),
                            atributos_elegidos.get('precision', 0),
                            atributos_elegidos.get('velocidad', 0),
                            atributos_elegidos.get('defensa', 0))
        if i == 0:
            personaje1 = personaje
        else:
            personaje2 = personaje

        print(f'\nResumen de tu personaje:\n{personaje}')

    simulaBatalla(personaje1, personaje2)

    respuesta = input("¿Quieres volver a jugar? (S/N)").lower()
    if respuesta == "s":
        continuar = True
    else:
        continuar = False

print("¡Gracias por jugar!")