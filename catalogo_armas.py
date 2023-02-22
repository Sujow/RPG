import bancos

espada_pouco_afiada = {'nome':'ESPADA POUCO AFIADA LVL(1)','atk':15,'defesa':0,'power':0,
                       'life':0, 'mana':0, 'penetracao_magica':0,'critico':2,'espaço':3}

espada_afiada = {'nome':'ESPADA AFIADA LVL(2)','atk':25,'defesa':0,'power':0,
                 'life':0, 'mana':0, 'penetracao_magica':0,'critico':8,'espaço':3}

espada_aco_nobre = {'nome':'ESPADA DE AÇO NOBRE LVL(3)','atk':45,'defesa':0,'power':0,
                    'life':0, 'mana':0, 'penetracao_magica':0,'critico':15,'espaço':2}

espada_valiriana = {'nome':'ESPADA DE AÇO VALIRIANO LVL(4)','atk':60,'defesa':0,'power':0,
                    'life':0, 'mana':0, 'penetracao_magica':0,'critico':35,'espaço':2}

espada_de_dagrao = {'nome':'ESPADA AÇO DE DRAGÃO LVL(5)','atk':70,'defesa':0,'power':20,
                    'life':0, 'mana':0, 'penetracao_magica':10,'critico':25,'espaço':2}

#= CAJADOS ============================================================

cajado_de_madeira = {'nome':'CAJADO DE MADEIRA LVL(1)','atk':1,'defesa':0,'power':20,
                     'life':0, 'mana':0, 'penetracao_magica':0,'critico':2,'espaço':4}

cajado_de_metal = {'nome':'CAJADO DE METAL LVL(2)','atk':5,'defesa':0,'power':30,
                   'life':0, 'mana':0, 'penetracao_magica':10,'critico':4,'espaço':5}

cajado_anciao = {'nome':'CAJADO DE MAGO ANCIÃO LVL(3)','atk':5,'defesa':0,'power':50,
                 'life':0, 'mana':0, 'penetracao_magica':25,'critico':4,'espaço':5}

cajado_sombrio = {'nome':'CAJADO SOMBRIO LVL(4)','atk':5,'defesa':0,'power':70,
                  'life':0, 'mana':0, 'penetracao_magica':50,'critico':4,'espaço':5}

cajado_gandalf = {'nome':'CAJADO SUMPREMO DE GANDALF LVL(5)','atk':5,'defesa':0,'power':99,
                  'life':0, 'mana':0, 'penetracao_magica':25,'critico':4,'espaço':5}

#= BOTAS ============================================================

bota_de_couro = {'nome':'BOTA DE COURO LVL(1)','atk':0,'defesa':3,'power':0,
                 'life':0, 'mana':0, 'penetracao_magica':0,'critico':0,'espaço':1}

bota_couraca = {'nome':'BOTA COURAÇA LVL(2)','atk':0,'defesa':10,'power':0,
                'life':0, 'mana':0, 'penetracao_magica':0,'critico':0,'espaço':2}

bota_revestida = {'nome':'BOTA REVESTIDA LVL(3)','atk':0,'defesa':20,'power':0,
                  'life':0, 'mana':0, 'penetracao_magica':0,'critico':0,'espaço':2}

bota_guerreiro = {'nome':'BOTA DE GUERREIRO LVL(4)','atk':0,'defesa':40,'power':0,
                  'life':10, 'mana':0, 'penetracao_magica':0,'critico':0,'espaço':2}

bota_mago = {'nome':'BOTA DE MAGO LVL(5)','atk':0,'defesa':40,'power':0,
             'life':0, 'mana':10, 'penetracao_magica':0,'critico':0,'espaço':2}

#= ANEIS ============================================================

anel_magico = {'nome':'ANEL MAGICO LVL(1)','atk':0,'defesa':0,'power':5,
               'life':0, 'mana':1, 'penetracao_magica':1,'critico':0,'espaço':0}

anel_magico_anciao = {'nome':'ANEL MAGICO DO ANCIÃO LVL(2)','atk':0,'defesa':0,'power':10,
                      'life':0, 'mana':3, 'penetracao_magica':3, 'critico':0,'espaço':0}

anel_aprendiz = {'nome':'ANEL MAGO APRENDIZ LVL(3)','atk':0,'defesa':0,'power':20,
                 'life':0, 'mana':10, 'penetracao_magica':15, 'critico':0,'espaço':0}

anel_murdok = {'nome':'ANEL DE MURDOK LVL(4)','atk':0,'defesa':15,'power':35,
               'life':0, 'mana':15, 'penetracao_magica':40, 'critico':0,'espaço':0}

anel_poder = {'nome':'ANEL DO PODER LVL(5)','atk':0,'defesa':0,'power':50,
              'life':10, 'mana':20, 'penetracao_magica':15, 'critico':0,'espaço':0}

#= VESTIMENTAS ============================================================

manto_simples = {'nome':'MANTO SIMPLES LVL(1)','atk':0,'defesa':5,'power':0,
                 'life':1, 'mana':0, 'penetracao_magica':0, 'critico':0,'espaço':2}

manto_aprimorado = {'nome':'MANTO APRIMORADO LVL(2)','atk':0,'defesa':15,'power':0,
                    'life':5, 'mana':0, 'penetracao_magica':0, 'critico':0,'espaço':3}

manto_real = {'nome':'MANTO REAL LVL(3)','atk':0,'defesa':25,'power':0,
              'life':15, 'mana':0, 'penetracao_magica':0, 'critico':0,'espaço':4}

manto_armog = {'nome':'MANTO ARMOG LVL(4)','atk':0,'defesa':45,'power':0,
              'life':20, 'mana':0, 'penetracao_magica':0, 'critico':0,'espaço':4}

manto_life = {'nome':'MANTO LIFE LVL(5)','atk':0,'defesa':20,'power':0,
              'life':45, 'mana':0, 'penetracao_magica':0, 'critico':0,'espaço':4}

    
espadas = {1:espada_pouco_afiada,2:espada_afiada,3:espada_aco_nobre,
           4:espada_valiriana,5:espada_de_dagrao}

cajados = {1:cajado_de_madeira,2:cajado_de_metal,3:cajado_anciao,
           4:cajado_sombrio,5:cajado_gandalf}

botas = {1:bota_de_couro,2:bota_couraca,3:bota_revestida,
         4:bota_guerreiro,5:bota_mago}

aneis = {1:anel_magico,2:anel_magico_anciao,3:anel_aprendiz,
         4:anel_murdok,5:anel_poder}

vestimenta = {1:manto_simples,2:manto_aprimorado,3:manto_real,
              4:manto_armog,5:manto_life}

##for k in espadas:
##    itens = espadas[k]
##
##    bancos.insere_arma_arsenal(itens['nome'], atk=itens['atk'],defesa=itens['defesa'],
##           power=itens['power'],life=itens['life'],mana=itens['mana'],
##           penetracao_magica=itens['penetracao_magica'],critico=itens['critico'], espaço=itens['espaço'])

for k in cajados:
    itens = cajados[k]

    bancos.insere_arma_arsenal(itens['nome'], atk=itens['atk'],defesa=itens['defesa'],
           power=itens['power'],life=itens['life'],mana=itens['mana'],
           penetracao_magica=itens['penetracao_magica'],critico=itens['critico'], espaço=itens['espaço'])

for k in botas:
    itens = botas[k]

    bancos.insere_arma_arsenal(itens['nome'], atk=itens['atk'],defesa=itens['defesa'],
           power=itens['power'],life=itens['life'],mana=itens['mana'],
           penetracao_magica=itens['penetracao_magica'],critico=itens['critico'], espaço=itens['espaço'])

for k in aneis:
    itens = aneis[k]

    bancos.insere_arma_arsenal(itens['nome'], atk=itens['atk'],defesa=itens['defesa'],
           power=itens['power'],life=itens['life'],mana=itens['mana'],
           penetracao_magica=itens['penetracao_magica'],critico=itens['critico'], espaço=itens['espaço'])

for k in vestimenta:
    itens = vestimenta[k]

    bancos.insere_arma_arsenal(itens['nome'], atk=itens['atk'],defesa=itens['defesa'],
           power=itens['power'],life=itens['life'],mana=itens['mana'],
           penetracao_magica=itens['penetracao_magica'],critico=itens['critico'], espaço=itens['espaço'])
