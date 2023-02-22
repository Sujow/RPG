import socket
import main

#from gamestate import GameState

# Cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind no endereco e porta
server_address = ('localhost', 50000)
sock.bind(server_address)

# Fica ouvindo por conexoes
sock.listen(1)

connection, client_address = sock.accept()


a = "A BATALHA COMEÇA"
connection.sendall(a).encode('utf-8')
nome = connection.sendall("Diga o seu Nick name: ").encode('utf-8')
nome1 = ""
tipo = connection.sendall("Qual a sua classe? ").encode('utf-8')


##while True:
##
##    print('Aguardando a conexao do jogador')
##    connection, client_address = sock.accept()
##
##    try:
##        print('Jogador chegou! :)')
##
##        # Cria um tabuleiro de jogo vazio
##        partida = main
##
##        # Processa em loop
##        while True:
##            # Recebe a jogada do jogador
##            data = connection.recv(1024)
##
##            # Checa se a conexao do jogador foi terminada
##            if "pp" in data:
##                print('Jogador se foi. :(')
##                break
##
##            # Envia o tabuleiro para o jogador
##            connection.sendall(partida.batalha().encode('utf-8'))
##
####            print('O jogador jogou:')
####            board.print()
##
##        
##    finally:
##        # Clean up the connection
##        connection.close()

##while True:
##
##    print('Aguardando a conexao do jogador')
##    connection, client_address = sock.accept()
##
##    try:
##        print('Jogador chegou! :)')
##
##        # Cria um tabuleiro de jogo vazio
##        board = GameState()
##
##        # Faz uma jogada aleatoria
##        board.moveRandom('o')
##        print('Eu joguei:')
##        board.print()
##
##        # Envia o tabuleiro para o jogador
##        connection.sendall(board.save().encode('utf-8'))
##
##        # Processa em loop
##        while True:
##            # Recebe a jogada do jogador
##            data = connection.recv(1024)
##
##            # Checa se a conexao do jogador foi terminada
##            if not data:
##                print('Jogador se foi. :(')
##                break
##
##            # Converte para string e restaura no tabuleiro
##            board.restore(data.decode('utf-8'))
##
##            print('O jogador jogou:')
##            board.print()
##
##            # Faz outra jogada aleatoria
##            board.moveRandom('o')
##            print('Eu joguei:')
##            board.print()
##
##            # Envia o tabuleiro para o jogador
##            connection.sendall(board.save().encode('utf-8'))
##
##    finally:
##        # Clean up the connection
##        connection.close()
