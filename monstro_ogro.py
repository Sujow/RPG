import random
from time import sleep

class Ogro:
    def __init__(self):
        self.name = "OGRO"
        self.tipo = "ORG"
        self.mana = 0
        self.defesa = 60
        self.resistencia_magica = 40
        self.atack_fisico = 55
        self.power = 10
        self.life = 80
        self.mana_regen = 0
        self.bag = 100
        self.penetração_magica = 0
        self.critico = 20

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
            dano = random.randint(10,50)
            print("SOCO DE PEDRA!!!")
            sleep(2)
            print(f"DANO = {dano}")
            print("_"*25)
            return dano
            
        if escolha == 5:
            dano = random.randint(20,55)
            print("OGRO ESMAGA!!!")
            sleep(2)
            print(f"DANO = {dano}")
            print("_"*25)
            return dano
        
        
















    
