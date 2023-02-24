import bancos
import mainn

def menu(nome):

    print("Bem vindo ao Invetario! Escolha uma das opções:")
    
    while True:
        print("[1] Exibir todos os itens")
        print("[2] Equipar")
        print("[3] Equipados")
        print("[4] Deletar")
        print("[5] Retornar")
        opcao = int(input("Digite o número da opção: "))

        bag = bancos.exibe_inventario(nome)

        if opcao == 1:
            n = 0
            for i in bancos.exibe_inventario(nome):
                print(f'NOME: {i[1]} {n}')
                print(f'ATKE: {i[2]} | DEFE: {i[3]}')
                print(f'POWE: {i[4]} | LIFE: {i[5]}')
                print(f'CRIT: {i[8]} | MANA: {i[6]}')
                print(f'PMAG: {i[7]} | ESPA: {i[9]}')
                print("="*15)
                n+=1

        elif opcao == 2:

            #Cria a tebela dos itens equipado caso n exista para o user
            bancos.tab_itens_equipados(nome)

            while True:
                print("_"*25)
                print("[1] Corpo")
                print("[2] Mão Arma")
                print("[3] Mão Anel")
                print("[4] Pés")
                print("[5] lote Retornar")

                dic_lote = {1:"corpo",2:"mao_arma",3:"mao_anel",4:"pes"}
                
                lote = int(input("Qual lote gostaria de equipar?: "))

                if lote == 5:
                    break
                
                item = int(input("Qual o indice do item?: "))

                bancos.equipa_item(nome,bag[item][1],dic_lote[lote])
                print(f'nome {nome}, bag {bag[item][1]}, dic {dic_lote[lote]}')

        elif opcao == 3:
            try:
                print(f'Corpo: {bancos.exibe_equipados(nome)[0][3]}')
            except Exception as err:
                print(f'Corpo:')
            try:
                print(f'Mão Arma: {bancos.exibe_equipados(nome)[0][1]}')
            except Exception as err:
                print(f'Mão Arma:')
            try:
                print(f'Mão Anel: {bancos.exibe_equipados(nome)[0][2]}')
            except Exception as err:
                print(f'Mão Anel:')                
            try:
                print(f'PÉS: {bancos.exibe_equipados(nome)[0][4]}')
            except Exception as err:
                print(f'PÉS:')
                
        elif opcao == 4:    
            print("_"*25)
            equipar = input("Digite o indice dos itens que deseja deletar: ")

        elif opcao == 5:
            mainn.menu()
            break
            
