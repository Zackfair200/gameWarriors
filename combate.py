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

while continuar:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Selecciona la clase de tu personaje: ")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Picaro")
    clase_elegida = int(input("Ingresa el número de la clase elegida: "))

    if clase_elegida == 1:
        clase1 = Clase("Guerrero",20, 7, 3, 3, 4)
    elif clase_elegida == 2:
        clase1 = Clase("Mago",15, 5, 8, 4, 2)
    elif clase_elegida == 3:
        clase1 = Clase("Pícaro",10, 4, 6, 6, 2)
    else:
        print("Selección inválida")

    os.system('cls' if os.name == 'nt' else 'clear')

    print("🥋 PRIMER PARTICIPANTE 🥊")
    name1 = input("Ingresa el nombre de tu personaje: ")
    life1 = int(input(f"Ingresa la vida de {name1}: "))
    strength1 = int(input(f"Ingresa la fuerza de {name1}: "))
    precision1 = int(input(f"Ingresa la precisión de {name1}: "))
    speed1 = int(input(f"Ingresa la velocidad de {name1}: "))
    defense1 = int(input(f"Ingresa la defensa de {name1}: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Selecciona la clase de tu personaje: ")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Picaro")
    clase_elegida = int(input("Ingresa el número de la clase elegida: "))

    if clase_elegida == 1:
        clase2 = Clase("Guerrero",20, 7, 3, 3, 4)
    elif clase_elegida == 2:
        clase2 = Clase("Mago",15, 5, 8, 4, 2)
    elif clase_elegida == 3:
        clase2 = Clase("Pícaro",10, 4, 6, 6, 3)
    else:
        print("Selección inválida")

    os.system('cls' if os.name == 'nt' else 'clear')

    print("💪 SEGUNDO PARTICIPANTE 🤸‍♂️")
    name2 = input(f"Ingresa el nombre de tu personaje: ")
    life2 = int(input(f"Ingresa la vida de {name2}: "))
    strength2 = int(input(f"Ingresa la fuerza de {name2}: "))
    precision2 = int(input(f"Ingresa la precisión de {name2}: "))
    speed2 = int(input(f"Ingresa la velocidad de {name2}: "))
    defense2 = int(input(f"Ingresa la defensa de {name2}: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    jugador1 = Character(clase1, name1, life1, strength1, precision1, speed1, defense1)
    jugador2 = Character(clase2, name2, life2, strength2, precision2, speed2, defense2)

    simulaBatalla(jugador1, jugador2)

    respuesta = input("¿Quieres volver a jugar? (S/N)").lower()
    if respuesta == "s":
        continuar = True
    else:
        continuar = False

print("¡Gracias por jugar!")