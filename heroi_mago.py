import random
from time import sleep
import bancos


class mago:
    def __init__(self, name, tipo):
        self.name = name
        self.tipo = tipo
        self.mana = 55
        self.defesa = 30
        self.atack_fisico = 15
        self.power = 40
        self.life = 50
        self.mana_regen = 15
        self.bag = 100
        self.penetração_magica = 35
        self.critico = 3

    def atack(self, escolha, power, mana_regen, mana, penetração_magica):

        penetrou = ""

        if escolha == 1:
            custo_mana = 15
            if mana >= custo_mana:
                mana_nova = mana - custo_mana
                mana_gasta = mana - custo_mana
                dano = random.randint(10,50)

                dano_magico = dano + power

                pen_m = random.randint(1,100)
                if pen_m <= penetração_magica:
                    penetração_mag = 1 #penetrou 100% critico magico
                    print(f"PENETRAÇÃO {pen_m}")
                    mana_regen += 15
                    mana_nova += mana_regen
                    penetrou = "sim"
                    
                else:
                    penetração_mag = 0 #sem penetração
                    print(f"SEM PENETRAÇÃO {pen_m}")
                    mana_nova += mana_regen
                    penetrou = "não"


                print("FOGO!!!")
                sleep(1)
                print(f"DANO = {dano_magico}, Mana restante = {mana_gasta}")
                print(f'Mana regenadara {mana_regen}')
                #self.mana += self.mana_regen
                print(f'Mana restante {mana_nova}')            
                
                return dano_magico, mana_nova, penetrou, pen_m
            
            else:
                mana += mana_regen
                print("Droga! Sem mana...")
                return 0,mana_nova, penetrou, pen_m
            
        if escolha == 2:
            custo_mana = 25
            if mana >= custo_mana:
                mana_nova = mana - custo_mana
                mana_gasta = mana - custo_mana
                dano = random.randint(15,55)
                
                dano_magico = dano + power

                pen_m = random.randint(1,100)
                if pen_m <= penetração_magica:
                    penetração_mag = 1 #penetrou 100% critico magico
                    mana_regen += 15
                    mana_nova += mana_regen
                else:
                    penetração_mag = 0 #sem penetração
                    mana_nova += mana_regen
                
                print("RAIO!!!")
                sleep(1)
                print(f"DANO = {dano_magico}, Mana restante = {mana_gasta}")
                print(f'Mana regenadara {mana_regen}')
                #self.mana += self.mana_regen
                print(f'Mana restante {mana_nova}')

                return dano_magico, mana_nova, penetrou, pen_m
            
            else:
                mana += mana_regen
                print("Droga! Sem mana...")
                return 0, mana_nova, penetrou, pen_m     

        if escolha == 3:
            custo_mana = 30
            if mana >= custo_mana:
                mana_nova = mana - custo_mana
                mana_gasta = mana - custo_mana
                dano = random.randint(30,60)
                
                dano_magico = dano + power

                pen_m = random.randint(1,100)
                if pen_m <= penetração_magica:
                    penetração_mag = 1 #penetrou 100% critico magico
                    mana_regen += 15
                    mana_nova += mana_regen
                else:
                    penetração_mag = 0 #sem penetração
                    mana_nova += mana_regen
                  
                print("OLHA A PEDRA!!!")
                sleep(1)
                print(f"DANO = {dano_magico}, Mana restante = {mana_gasta}")
                print(f'Mana regenadara {mana_regen}')
                #self.mana += self.mana_regen
                print(f'Mana restante {mana_nova}')
                
                return dano_magico, mana_nova, penetrou, pen_m
            else:
                mana += mana_regen
                print("Droga! Sem mana...")
                return 0, mana_nova, penetrou, pen_m


        if escolha == 4:
            custo_mana = 35
            aguarde = {}
            if mana >= custo_mana:
                mana = mana - custo_mana
                tempo = random.randint(1,2)
                print("STUN!!!")
                sleep(1)
                print(f"TEMPO DO STUN = {tempo}, Mana restante = {mana}")
                print(f'Mana regenadara {mana_regen}')
                mana += mana_regen
                print(f'Mana restante {mana}')
                aguarde["sim"] = tempo
                return aguarde, mana,penetrou
            else:
                mana += mana_regen
                print("Droga! Sem mana...")
                return 0, mana, penetrou

    def ultmate(self):
        custo_mana = 80
        if mana >= 80:
            mana = mana - custo_mana
            dano = random.randint(86,100)

            dano_magico = dano + power
            
            pen_m = random.randint(1,100)
            if pen_m <= penetração_magica:
                penetração_mag = 1 #penetrou 100% critico magico
                mana_regen += 15
                mana += mana_regen
            else:
                penetração_mag = 0 #sem penetração
                mana += mana_regen

            print(f"AAAAAAAAAAHHHHH")
            sleep(1)
            print('TOMA!!!!!')
            sleep(0.5)
            print(f'DANO = {dano_magico}, {self.mana}')
            
            return dano_magico, penetração_mag
        else:
            mana += mana_regen
            print("Droga! Sem mana...")
            return 0


















    
