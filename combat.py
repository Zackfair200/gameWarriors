import json
import random
import time
import os
import logging
from playsound import playsound


class Combate:
    def __init__(self, atacante: str, defensor: str) -> None:
        self.atacante = atacante
        self.defensor = defensor
        self.hits = []
        self.resultado = None

    def agregar_golpe(self, golpe):
        self.hits.append(golpe)

    def establecer_resultado(self, resultado):
        self.resultado = resultado

    def a_json(self):
        datos = {
            "atacante": self.atacante,
            "defensor": self.defensor,
            "hits": self.hits,
            "resultado": self.resultado
        }
        return json.dumps(datos)
    
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
        golpes = []
        # Empieza la pelea
        while warrior1.stayAlive() and warrior2.stayAlive():
            resultado_golpe = golpeador.hit(receptor)
            golpes.append(resultado_golpe)
            golpeExtra += warrior1.speed
            if golpeExtra >= limite:
                print("Ataque extra!")
                resultado_golpe = golpeador.hit(receptor)
                golpes.append(resultado_golpe)
                golpeExtra -= 50
            golpeador, receptor = receptor, golpeador

        
        # Muestro el resultado de la pelea
        winner = ""
        if warrior1.life <= 0:
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.debug(f"{warrior2.name} ES EL GANADOR!! 🏆")
            playsound("sound/you.mp3")
            playsound("sound/win.mp3")
            winner = warrior2.name
            time.sleep(1)
        elif warrior2.life <= 0:
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.debug(f"{warrior1.name} ES EL GANADOR!! 🏆")
            playsound("sound/you.mp3")
            playsound("sound/win.mp3")
            winner = warrior1.name
            experience = (warrior2.level * 10)/2
            warrior1.ganar_combate(experience)
            print(f"{warrior1.name} ha ganado {warrior1.experience}/{warrior1.next_level} más para alcanzar el siguiente nivel.")
            time.sleep(1)


        objeto_final = {
            "atacante" : golpes[0]['atacante'],
            "defensor" : golpes[0]['defensor'],
            "hits": golpes,
            "vencedor": winner
        }
        print(f"{objeto_final}")
