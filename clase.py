

class Clase():
    def __init__(self, name, mod_life, mod_strength, mod_accuracy, mod_speed, mod_defense, block=False):
        self.nombre = name
        self.modLife = mod_life
        self.modStrength = mod_strength
        self.modAccurancy = mod_accuracy
        self.modSpeed = mod_speed
        self.modDefense = mod_defense
        self.hits_received = 0
        self.shield_on = False
        self.block = block


    def shieldLock(self, enemy):
        # Incrementar el contador de golpes recibidos
        enemy.clase.hits_received += 1
        # Activar el bloqueo después de recibir cinco golpes
        if enemy.clase.hits_received == 5:
            print(f"{enemy.name} ha activado su bloqueo de escudo.")
            print("-------------------------------")
            enemy.clase.shield_on = True

    def reset_shield_lock(self):
        # Reiniciar el contador de golpes recibidos después de cada combate
        self.hits_received = 0
        self.shield_on = False