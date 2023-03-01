import random
from time import sleep

class Ogro:
    def __init__(self):
        self.name = "OGRO LVL 2"
        self.tipo = "ORG"
        self.mana = 0
        self.defesa = 90 #sempre +50% por lvl
        self.resistencia_magica = 60
        self.atack_fisico = 82.5
        self.power = 15
        self.life = 120
        self.mana_regen = 0
        self.bag = 100
        self.penetração_magica = 0
        self.critico = 30

    def ultmate(self):
        dano = random.randint(50,60)
        print(f"MEGA PEDRADA")
        sleep(1)
        print('TOMA!!!!!')
        sleep(3)
        print(f"DANO = {dano}")
        print("_"*25)
        return dano


    def atack(self):

        escolha = random.randint(1,6)

        if escolha != 5:
            dano = random.randint(15,60)
            print("SOCO DE PEDRA!!!")
            sleep(2)
            print(f"DANO = {dano}")
            print("_"*25)
            
            critico = random.randint(1,100)
            if critico <= self.critico:
                penetração_cr = 1 #penetrou 100% critico magico
                print(f"PENETRAÇÃO {critico}")
                penetrou = "sim"
                
            else:
                penetração_cr = 0 #sem penetração
                print(f"SEM PENETRAÇÃO {critico}")
                penetrou = "não"

            return (dano + self.atack_fisico),penetrou
            
        if escolha == 5:
            dano = random.randint(20,45)
            print("OGRO ESMAGA!!!")
            sleep(2)
            print(f"DANO = {dano}")
            print("_"*25)

            critico = random.randint(1,100)
            if critico <= self.critico:
                penetração_cr = 1 #penetrou 100% critico magico
                print(f"PENETRAÇÃO {critico}")
                penetrou = "sim"
                
            else:
                penetração_cr = 0 #sem penetração
                print(f"SEM PENETRAÇÃO {critico}")
                penetrou = "não"

            return (dano + self.atack_fisico),penetrou














    
