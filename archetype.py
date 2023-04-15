import os


class BasicArchetype:
    def __init__(self, name, life, strength, precision, speed, defense):
        """Declaro los atributos de clase"""
        self.name = name
        self.life = 1
        self.strength = 1
        self.precision = 1
        self.speed = 1
        self.defense = 1 
        self.dodge = 1
        self.level = 1
        self.experience = 0
        self.next_level = 50 + (self.level * 10)

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