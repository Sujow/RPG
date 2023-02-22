import sqlite3

conn = sqlite3.connect("dados.db")
cursor = conn.cursor()
tabs = []
dic_inv_equipado = {"Mão Direita":"","Mão Esquerda":"",
                    "Corpo": "","Pés": ""}

def tabela_user(nome):
    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {nome}_CHAR (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_user TEXT NOT NULL,
        classe TEXT NOT NULL,
        atk INTEGER NOT NULL,
        defesa INTEGER NOT NULL,
        power INTEGER NOT NULL,
        life INTEGER NOT NULL,
        mana INTEGER NOT NULL,
        penetração_magica INTEGER NOT NULL,
        critico INTEGER NOT NULL);""")

    except:
        pass

def tabela_iventario(nome):
    
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome}_IVENTARIO (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    atk INTEGER NOT NULL,
    defesa INTEGER NOT NULL,
    power INTEGER NOT NULL,
    life INTEGER NOT NULL,
    mana INTEGER NOT NULL,
    penetração_magica INTEGER NOT NULL,
    critico INTEGER NOT NULL,
    espaço INTEGER NOT NULL);""")


def tab_itens_equipados(nome):
    
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome}_equipado (
    id INTEGER NOT NULL PRIMARY KEY,
    mao_arma,
    mao_anel,
    corpo,
    pes);""")

def tabela_arsenal():
    
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS arsenal (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    atk INTEGER NOT NULL,
    defesa INTEGER NOT NULL,
    power INTEGER NOT NULL,
    life INTEGER NOT NULL,
    mana INTEGER NOT NULL,
    penetração_magica INTEGER NOT NULL,
    critico INTEGER NOT NULL,
    espaço INTEGER NOT NULL);""")


def insere_inventario(nome, itemm,atk=0,defesa=0,
           power=0,life=0,mana=0,
           penetracao_magica=0,critico=0, espaço=0):
    
    # inserindo dados na tabela
    cursor.execute(f"""
    INSERT OR REPLACE INTO {nome}_IVENTARIO (item,atk,defesa,power,life,mana,penetração_magica,critico, espaço)
    VALUES ('{itemm}',{atk},{defesa},{power},{life},{mana},{penetracao_magica},{critico},{espaço})""")

    # gravando no bd
    conn.commit()


def insere_user(nome, nome_user,classe,atk=0,defesa=0,
           power=0,life=0,mana=0,
           penetracao_magica=0,critico=0):
    
    # inserindo dados na tabela
    cursor.execute(f"""
    INSERT OR REPLACE INTO {nome}_CHAR (nome_user,classe,atk,defesa,power,life,mana,penetração_magica,critico)
    VALUES ('{nome_user}','{classe}',{atk},{defesa},{power},{life},{mana},{penetracao_magica},{critico})""")

    # gravando no bd
    conn.commit()

def insere_arma_arsenal(itemm,atk=0,defesa=0,
           power=0,life=0,mana=0,
           penetracao_magica=0,critico=0, espaço=0):
    
    # inserindo dados na tabela
    cursor.execute(f"""
    INSERT OR REPLACE INTO arsenal (item,atk,defesa,power,life,mana,penetração_magica,critico, espaço)
    VALUES ('{itemm}',{atk},{defesa},{power},{life},{mana},{penetracao_magica},{critico},{espaço})""")

    # gravando no bd
    conn.commit()

def busca_arma_arsenal(arma):
    cursor.execute(f"SELECT * FROM arsenal WHERE item = '{arma}'")
    resultado = cursor.fetchall()
    return resultado

def exibe_inventario(nome):
    global tabs
    try:
        cursor.execute(f"SELECT * FROM {nome}_IVENTARIO")
        tabs = cursor.fetchall()
        return tabs
    except:
        print("User sem inventário")


def equipa_item(nome, item, lote):
    cursor.execute(f"UPDATE {nome}_equipado SET '{lote}' = '{item}' WHERE ID = 1")

    # gravando no bd
    conn.commit()

def exibe_equipados(nome):
    try:
        cursor.execute(f"SELECT * FROM {nome}_equipado")
        tabs = cursor.fetchall()
        return tabs
    except:
        print("User sem lotes")




    
