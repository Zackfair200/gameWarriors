import random
import time
import os
from playsound import playsound
from archetype import BasicArchetype


class Warrior(BasicArchetype):
    def __init__(self, name, life, strength, precision, speed, defense):
        super().__init__(name, life, strength, precision, speed, defense)
        self.life = (self.life + life) * 20
        self.strength = (self.strength + strength) * 5
        self.precision = (self.precision + precision)
        self.speed = (self.speed + speed) * 1
        self.defense = (self.defense + defense) * 3
        self.hits_received = 0
        self.shield_on = False

    def hit(self, enemy):
        # comprobar si el ataque impacta
        if random.randint(1, 100) >= enemy.dodge:
            print(f"{self.name} ataca.")
            # Comprobar si el bloqueo está activado y desactivarlo después del siguiente golpe
            if enemy.shield_on:
                print(f"{enemy.name} bloquea el ataque.")
                playsound("sound/woodBlock.mp3")
                enemy.shield_on = False
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
                self.shieldLock(enemy)
        else:
            print(f"{self.name} ataca.")
            print(f"{enemy.name} ha esquivado el golpe.")
            playsound("sound/evade.mp3")
            time.sleep(1)
            print("-------------------------------")

    def shieldLock(self, enemy):
        # Incrementar el contador de golpes recibidos
        enemy.hits_received += 1
        # Activar el bloqueo después de recibir cinco golpes
        if enemy.hits_received == 5:
            print(f"{enemy.name} ha activado su bloqueo de escudo.")
            print("-------------------------------")
            enemy.shield_on = True

    def reset_shield_lock(self):
        # Reiniciar el contador de golpes recibidos después de cada combate
        self.hits_received = 0
        self.shield_on = False


