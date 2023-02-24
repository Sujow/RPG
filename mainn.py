import random
from time import sleep
import sqlite3
from monstros import monstro_ogro1, monstro_ogro2
import heroi_mago
import bancos
import gerador_item
import menu_iventario

def menu():
    global nome, tipo
    nome = input("Diga o seu Nick name: ")
    tipo = input("Qual a sua classe? ")

    print("O que deseja fazer?")
    print("[1] Acessar Iventario;\n[2] Batalhar")
    menu_escolha = int(input("Digite o número da opção: "))

    if menu_escolha == 1:
        menu_iventario.menu(nome)
    elif menu_escolha == 2:
        batalha()

def batalha():
    level = 1

    meu_char = heroi_mago.mago(nome,tipo)
    char_base = heroi_mago.mago(nome,tipo)
    
    monstro = monstro_ogro1.Ogro()

    bancos.tab_itens_equipados(nome)
    
    equipados = bancos.exibe_equipados(nome)

    atk = 0
    defesa = 0
    life = 0
    power = 0
    mana = 0
    penetração_M = 0
    critico = 0

    #print(equipados[0])
    print("\n--------EQUIPADOS------------------")
    if equipados != None or equipados != "None":
        for n,i in enumerate(equipados[0]):
            nome_item = equipados[0][n]
            print(nome_item)
            if nome_item != 1:
                try:
                    meu_char.atack_fisico += bancos.busca_arma_arsenal(nome_item)[0][2]
                    meu_char.defesa += bancos.busca_arma_arsenal(nome_item)[0][3]
                    meu_char.power += bancos.busca_arma_arsenal(nome_item)[0][4]
                    meu_char.life += bancos.busca_arma_arsenal(nome_item)[0][5]
                    vida_restaurada = meu_char.life
                    meu_char.mana += bancos.busca_arma_arsenal(nome_item)[0][6]
                    mana_restaurada = meu_char.mana
                    meu_char.penetração_magica += bancos.busca_arma_arsenal(nome_item)[0][7]
                    meu_char.critico += bancos.busca_arma_arsenal(nome_item)[0][8]
                except:
                    pass

    print("\n========== Status do Heroi ============")
    print(f"ATKK: {char_base.atack_fisico} => {meu_char.atack_fisico}")
    print(f"DEFE: {char_base.defesa} => {meu_char.defesa}")
    print(f"LIFE: {char_base.life} => {meu_char.life}")
    print(f"POWE: {char_base.power} => {meu_char.power}")
    print(f"MANA: {char_base.mana} => {meu_char.mana}") 
    print(f"PMAG: {char_base.penetração_magica} => {meu_char.penetração_magica}")
    print(f"CRIT: {char_base.critico} => {meu_char.critico}")

    continua_gam = "n"
    print("\nA BATALHA COMEÇA")
    print(monstro.name)
    print("==============================")

    vida_heroi = meu_char.life
    presentação_vida_heroi = "-" * vida_heroi
        
    vida_monstro = monstro.life
    defesa_monstro = monstro.defesa
    resistencia_magc = monstro.resistencia_magica
    presentação_vida_monstro = "-" * vida_monstro

    print(f"\nSua Vida: {presentação_vida_heroi}| {vida_heroi}")
    print(f"\nVida monstro: {presentação_vida_monstro}| {vida_monstro}")
    
    cont_stun = 0
    while True:

        if continua_gam == "s":
            if level == 2:
                monstro = monstro_ogro2.Ogro()
            if level == 3:
                monstro = monstro_ogro3.Ogro()
            
            vida_heroi = meu_char.life
            meu_char.mana = mana_restaurada
            presentação_vida_heroi = "-" * vida_heroi
            
            vida_monstro = monstro.life
            defesa_monstro = monstro.defesa
            resistencia_magc = monstro.resistencia_magica
            presentação_vida_monstro = "-" * vida_monstro
            continua_gam = "n"
            print(monstro.name)
        
        print("_"*25)
        print(f'\nMana do Heroi = {meu_char.mana}')
        ação = input("\nComando atack (1) ou ULT (2, mana 80) :")

        if ação == "1":
            print("\n[1] Bola de fogo |Dano = (10 a 50)|Mana = 15")
            print("[2] Raio |Dano = (15 a 55)|Mana = 25")
            print("[3] Chuva de pedra |Dano = (30 a 60)|Mana = 30")
            print("[4] Stun |Tempo Stun = (1 a 2)|Mana = 35")
            print("_"*25)
            escolha = int(input("Escolha uma habilidade para usar "))
            print("_"*25)
            
            retorno = meu_char.atack(escolha, meu_char.power, meu_char.mana_regen, meu_char.mana, meu_char.penetração_magica)
            dano_da_porrada = retorno[0]

            if escolha == 4:
                print("STUNADO")
                cont_stun = 1
                    
            if retorno[2] == "sim":#penetrou critico
                print("<==== CRITICO ====>")
                vida_monstro -= dano_da_porrada

            if retorno[2] == "não":#NÃO penetrou
                if dano_da_porrada > resistencia_magc:
                    vida_monstro = vida_monstro + resistencia_magc - dano_da_porrada
                else:
                    print("O OGRO DEFENDEU!!!")

            print("Vido o Monstro: ", vida_monstro)
            print("-"*vida_monstro)
            meu_char.mana = retorno[1]
                            
        if ação == "2":
            pass

        if ação == "p":
            break

        if vida_monstro < 0:
            level += 1
            sleep(1)
            print("Você eliminou o Ogro das montanhas")
            sleep(2)
            print(f"## BAG DO OGRO ##")
            print("==============================")
            bag = gerador_item.gera_bag()
            
            bancos.tabela_user(nome)
            bancos.tabela_iventario(nome)


            for n,itemm in enumerate(bag):
                print(f'{itemm} {n}')

            ind_bag = list(input("Digite os indices,\nseparador por virgula,dos itens que gostaria adicionar a bag ").split(","))

            for itemm in ind_bag:
                
                bancos.insere_inventario(nome, bag[int(itemm)]['nome'],atk=bag[int(itemm)]['atk'],
                                         defesa=bag[int(itemm)]['defesa'],power=bag[int(itemm)]['power'],
                                         life=bag[int(itemm)]['life'],mana=bag[int(itemm)]['mana'],
                                         penetracao_magica=bag[int(itemm)]['penetracao_magica'],
                                         critico=bag[int(itemm)]['critico'],espaço=bag[int(itemm)]['espaço'])
            
            bancos.insere_user(nome, nome, tipo, atk= meu_char.atack_fisico,
                               defesa=meu_char.defesa, power=meu_char.power,
                               life=vida_heroi, mana=meu_char.mana,
                               penetracao_magica=meu_char.penetração_magica,
                               critico=meu_char.critico)
            
            continuar = input("\ndeseja continuar ? Digite [S/N]: ")
            if continuar.upper() == "S":
                continua_gam = "s"
                continue
            else:
                print("Finalizando...")
                sleep(15)
                break
        
        else:
            sleep(1)

            #MONSTRO ATACA
            if cont_stun == 0:
                print("O monstro vai atacar...")
                sleep(1)
                input("Digite N para prosseguir: ")
                opcao_monstro = random.randint(1,6)
                if opcao_monstro == 5:
                    opcao = monstro.ultmate()
                    print("_"*25)
                    vida_heroi -= opcao
                    presentação_vida_heroi = "||" * vida_heroi
                    sleep(1)
                    print(f"Vida Heroi: {presentação_vida_heroi}| {vida_heroi}")
                    print("_"*25)

                if opcao_monstro != 5:
                    opcao = monstro.atack()
                    print("_"*25)
                    if opcao[1] == "sim":#penetrou critico
                        vida_heroi -= opcao[0]
                    if opcao[1] == "não":#penetrou critico
                        vida_heroi = vida_heroi + meu_char.defesa - opcao[0]
                        
                    presentação_vida_heroi = "-" * vida_heroi
                    sleep(1)
                    print(f"Vida Heroi: {presentação_vida_heroi}| {vida_heroi}")
                    print("_"*25)

                if vida_heroi < 0:
                    sleep(1)
                    print("O Ogro te desimou..")
                    level = 0
                    continuar = input("deseja continuar ? Digite [S/N]: ")
                    if continuar.upper() == "S":
                        continua_gam = "s"
                    else:
                        print("Finalizando...")
                        sleep(15)
                        break
                else:
                    sleep(1)
                    print("É a sua vez...")
                    sleep(1)

            else:
                cont_stun += 1
                if vida_heroi < 0:
                    sleep(1)
                    print("O Ogro te desimou..")
                    level = 0
                    continuar = input("deseja continuar ? Digite [S/N]: ")
                    if continuar.upper() == "S":
                        continua_gam = "s"
                    else:
                        print("Finalizando...")
                        sleep(5)
                        break
                else:
                    sleep(1)
                    print("É a sua vez...")
                    sleep(1)

                if cont_stun > 2:
                    cont_stun = 0              

#batalha()
if __name__ == '__main__':
    menu()










    
