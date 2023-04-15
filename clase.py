

class Clase():
    def __init__(self, nombre, modLife, modStrength, modAccurancy, modSpeed, modDefense, block=False):
        self.nombre = nombre
        self.modLife = modLife
        self.modStrength = modStrength
        self.modAccurancy = modAccurancy
        self.modSpeed = modSpeed
        self.modDefense = modDefense
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