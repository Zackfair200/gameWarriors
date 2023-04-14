import random
import time
import os
from playsound import playsound


class Warrior:
    def __init__(self, name, life, strength, precision, speed, defense):
        """Declaro los atributos de clase"""
        self.name = name
        self.life = (1 + life) * 20
        self.strength = (1 + strength) * 5
        self.precision = (3 + precision)
        self.speed = (1 + speed) * 1
        self.dodge = 1
        self.defense = (1 + defense) * 3
        self.level = 1
        self.experience = 0
        self.next_level = 50 + (self.level * 10)

    def golpea(self, enemy):
        # comprobar si el ataque impacta
        if random.randint(1, 100) >= enemy.dodge:
            print(f"{self.name} ataca.")
            critical_hit_chance = min(1, max(0, self.precision / 100)) * 0.5
            print(f"Probabilidad de crítico: {critical_hit_chance*100}")
            if random.random() <= critical_hit_chance:
                damage = max((self.strength + self.dodge) - enemy.defense + random.randrange(-10, 11), 1)
                enemy.life -= damage
                print(f"{self.name} realiza un ataque crítico {damage} a {enemy.name} le quedan {enemy.life} puntos de vida 💥")
                playsound("sound/special.mp3")
                time.sleep(1)
            else:
                damage = max(self.strength - enemy.defense + random.randrange(-10, 11), 1)
                enemy.life -= damage
                print(f"{self.name} ha hecho {damage} puntos de daño y a {enemy.name} le quedan {enemy.life} puntos de vida 🤜")
                playsound("sound/punch.mp3")
                time.sleep(1)
            print("-------------------------------")
        else:
            print(f"{self.name} ataca.")
            print(f"{enemy.name} ha esquivado el golpe.")
            playsound("sound/evade.mp3")
            time.sleep(1)
            print("-------------------------------")

 
    def stayAlive(self):
        """Retorna True si el guerrero está vivo, False de lo contrario"""
        return self.life > 0
    
    def level_up(self):
        """Aumenta el nivel del guerrero y permite asignar puntos a los atributos"""
        self.level += 1
        self.next_level = self.level * 10
        points_to_assign = 5  # número de puntos para asignar a los atributos
        self.dodge += self.level // 5  # sumar +1 al atributo dodge por cada 5 niveles
        print(f"Felicidades, has subido al nivel {self.level}! Ahora tienes {points_to_assign} puntos para asignar a tus atributos.")
        while points_to_assign > 0:
            print(f"Atributos actuales:\n\t1. Vida: {self.life}\n\t2. Fuerza: {self.strength}\n\t3. Precisión: {self.precision}\n\t4. Velocidad: {self.speed}\n\t5. Esquivar: {self.dodge}\n\t6. Defensa: {self.defense}")
            attribute_choice = input("Elige un atributo para asignar un punto (1-6): ")
            if attribute_choice == "1":
                self.life += 5
                print("Se ha asignado un punto a Vida.")
            elif attribute_choice == "2":
                self.strength += 1
                print("Se ha asignado un punto a Fuerza.")
            elif attribute_choice == "3":
                self.precision += 1
                print("Se ha asignado un punto a Precisión.")
            elif attribute_choice == "4":
                self.speed += 1
                print("Se ha asignado un punto a Velocidad.")
            elif attribute_choice == "5":
                self.defense += 1
                print("Se ha asignado un punto a Defensa.")
            else:
                print("Esa no es una opción válida.")
                continue
            points_to_assign -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Te quedan {points_to_assign} puntos por asignar.")


    def ganar_combate(self, puntos_experiencia):
        self.experience += puntos_experiencia
        print(f"{self.name} ha ganado {puntos_experiencia} puntos de experiencia!")
        if self.experience >= self.next_level:
            self.lvl_up()


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
        golpeador.golpea(receptor)
        golpeExtra += warrior1.speed
        if golpeExtra >= limite:
            print("Ataque extra!")
            golpeador.golpea(receptor)
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

    print("🥋 PRIMER PARTICIPANTE 🥊")
    name1 = input("Ingresa el nombre del primer guerrero: ")
    life1 = int(input(f"Ingresa la vida de {name1}: "))
    strength1 = int(input(f"Ingresa la fuerza de {name1}: "))
    precision1 = int(input(f"Ingresa la precisión de {name1}: "))
    speed1 = int(input(f"Ingresa la velocidad de {name1}: "))
    defense1 = int(input(f"Ingresa la defensa de {name1}: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    print("💪 SEGUNDO PARTICIPANTE 🤸‍♂️")
    name2 = input(f"Ingresa el nombre del segundo guerrero: ")
    life2 = int(input(f"Ingresa la vida de {name2}: "))
    strength2 = int(input(f"Ingresa la fuerza de {name2}: "))
    precision2 = int(input(f"Ingresa la precisión de {name2}: "))
    speed2 = int(input(f"Ingresa la velocidad de {name2}: "))
    defense2 = int(input(f"Ingresa la defensa de {name2}: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    warrior1 = Warrior(name1, life1, strength1, precision1, speed1, defense1)
    warrior2 = Warrior(name2, life2, strength2, precision2, speed2, defense2)

    simulaBatalla(warrior1, warrior2)

    respuesta = input("¿Quieres volver a jugar? (S/N)").lower()
    if respuesta == "s":
        continuar = True
    else:
        continuar = False

print("¡Gracias por jugar!")
