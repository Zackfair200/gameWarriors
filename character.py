import os
import random
import time
from playsound import playsound
from clase import Clase
import logging


class Character:
    def __init__(self, clase: Clase, name: str, life: int, strength: int, precision: int, speed: int, defense: int) -> None:
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
        return f"Nombre: {self.name}\nClase: {self.clase.nombre}\nVida: {self.life}\nFuerza: {self.strength}\nPrecisión: {self.precision}\nVelocidad: {self.speed}\nDefensa: {self.defense}\nNivel: {self.level}\nExperiencia: {self.experience}/{self.next_level}"

        
    def setLife(self, lifePoints: int) -> None:
        self.life = lifePoints * self.clase.modVida

    def stayAlive(self):
        """Retorna True si el jugador está vivo, False de lo contrario"""
        return self.life > 0
    
    def level_up(self):
        """Aumenta el nivel del jugador y permite asignar puntos a los atributos"""
        self.level += 1
        self.next_level = self.level * 10
        self.dodge += self.level // 5  # sumar +1 al atributo dodge por cada 5 niveles
        points_to_assign = 5
        logger = logging.getLogger(__name__)
        logger.info(f"Felicidades, has subido al nivel {self.level}! Ahora tienes {points_to_assign} puntos para asignar a tus atributos.")
        attributes = ["Vida", "Fuerza", "Precisión", "Velocidad", "Defensa"]
        while points_to_assign > 0:
            print(f"Atributos actuales:")
            for i, attribute in enumerate(attributes):
                print(f"\t{i+1}. {attribute}: {getattr(self, attribute.lower())}")
            attribute_choice = input("Elige un atributo para asignar un punto (1-5): ")
            try:
                attribute_choice = int(attribute_choice)
                if attribute_choice < 1 or attribute_choice > 5:
                    raise ValueError
                attribute_name = attributes[attribute_choice-1].lower()
                setattr(self, attribute_name, getattr(self, attribute_name) + 1)
                print(f"Se ha asignado un punto a {attributes[attribute_choice-1]}.")
                points_to_assign -= 1
            except ValueError:
                print("Esa no es una opción válida.")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Te quedan {points_to_assign} puntos por asignar.")

    def ganar_combate(self, puntos_experiencia: int) -> None:
        self.experience += puntos_experiencia
        print(f"{self.name} ha ganado {puntos_experiencia} puntos de experiencia!")
        if self.experience >= self.next_level:
            self.lvl_up()

    def hit(self, enemy):
    # comprobar si el ataque impacta
        hit_success = random.randint(1, 100) >= enemy.dodge
        if hit_success:
            print(f"{self.name} ataca.")
            # Comprobar si el bloqueo está activado y desactivarlo después del siguiente golpe
            if enemy.clase.nombre == "Guerrero" and enemy.clase.shield_on:
                print(f"{enemy.name} bloquea el ataque.")
                playsound("sound/woodBlock.mp3")
                enemy.clase.shield_on = False
                return {
                    "atacante": self,
                    "defensor": enemy,
                    "golpe": "Bloqueo",
                    "resultado": ""
                }
            critical_hit_chance = min(1, max(0, self.precision / 100)) * 0.5
            print(f"Probabilidad de crítico: {critical_hit_chance*100}")
            if random.random() <= critical_hit_chance:
                damage = max((self.strength + self.dodge) - enemy.defense + random.randrange(-10, 11), 1)
                enemy.life -= damage
                print(f"{self.name} realiza un ataque crítico {damage} a {enemy.name} le quedan {enemy.life} puntos de vida 💥")
                playsound("sound/special.mp3")
                time.sleep(1)
                resultado = "Critico"
            else:
                damage = max(self.strength - enemy.defense + random.randrange(-10, 11), 1)
                enemy.life -= damage
                print(f"{self.name} ha hecho {damage} puntos de daño y a {enemy.name} le quedan {enemy.life} puntos de vida 🤜")
                playsound("sound/punch.mp3")
                time.sleep(1)
                resultado = "Normal"
            if enemy.clase.nombre == "Guerrero":
                self.clase.shieldLock(enemy)
        else:
            print(f"{self.name} ataca.")
            print(f"{enemy.name} ha esquivado el golpe.")
            playsound("sound/evade.mp3")
            time.sleep(1)
            print("-------------------------------")
            resultado = "Esquivado"

        return {
            "atacante": {
                "name": self.name,
                "life": self.life,
                "strength": self.strength,
                "precision": self.precision,
                "velocidad": self.speed,
                "defense": self.defense
            },
            "defensor": {
                "name": enemy.name,
                "life": enemy.life,
                "strength": enemy.strength,
                "precision": enemy.precision,
                "velocidad": enemy.speed,
                "defense": enemy.defense
            },
            "golpe": resultado,
            "resultado": {
                "vida_atacante": self.life,
                "vida_defensor": enemy.life
            }
        }
