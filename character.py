import os
import random
import time
from playsound import playsound

class Character:
    def __init__(self, clase, name, life, strength, precision, speed, defense):
        """Declaro los atributos de clase"""
        self.clase = clase
        self.name = name
        self.life = (1 + life) * self.clase.modLife
        self.strength = (1 + strength) * self.clase.modStrength
        self.precision = (1 + precision) * self.clase.modAccurancy
        self.speed = (1 + speed) * self.clase.modSpeed
        self.defense = (1 + defense) * self.clase.modDefense
        self.dodge = 1
        self.level = 1
        self.experience = 0
        self.next_level = 50 + (self.level * 10)

    def __str__(self):
        """Retorna la información del personaje en formato string"""
        return (f"Nombre: {self.name}\n"
                f"Clase: {self.clase.nombre}\n"
                f"Vida: {self.life}\n"
                f"Fuerza: {self.strength}\n"
                f"Precisión: {self.precision}\n"
                f"Velocidad: {self.speed}\n"
                f"Defensa: {self.defense}\n"
                f"Nivel: {self.level}\n"
                f"Experiencia: {self.experience}/{self.next_level}")

        
    def setLife(self,lifePoints):
        self.life = lifePoints * self.clase.modVida

    def stayAlive(self):
        """Retorna True si el jugador está vivo, False de lo contrario"""
        return self.life > 0
    
    def level_up(self):
        """Aumenta el nivel del jugador y permite asignar puntos a los atributos"""
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

    def hit(self, enemy):
        # comprobar si el ataque impacta
        if random.randint(1, 100) >= enemy.dodge:
            print(f"{self.name} ataca.")
            # Comprobar si el bloqueo está activado y desactivarlo después del siguiente golpe
            if enemy.clase.shield_on:
                print(f"{enemy.name} bloquea el ataque.")
                playsound("sound/woodBlock.mp3")
                enemy.clase.shield_on = False
                return
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
            self.clase.shieldLock(enemy)
        else:
            print(f"{self.name} ataca.")
            print(f"{enemy.name} ha esquivado el golpe.")
            playsound("sound/evade.mp3")
            time.sleep(1)
            print("-------------------------------")