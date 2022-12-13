import socket


def cliente_banco():
    host = socket.gethostname()  # utilizo esse comando pq estão ambos na mesma máquina
    port = 5001  #  numero da porta do servidor socket

    client_socket = socket.socket()  # inicia a instância do socket
    client_socket.connect((host, port))  # conecta no servidor

    message = input(" -> ")  # aguarda a entrada de dados

    while message.lower().strip() != 'finalizar': #se digitar finalizar, termina o programa para o cliente e o servidor tb
        client_socket.send(message.encode())  # envia a mensagem para o servidor
        data = client_socket.recv(1024).decode()  # recebe a resposta do servidor

        print('Received from server: ' + data)  # Mostra os dados recebidos no terminal

        message = input(" -> ")  # aguarda uma nova entrada de dados do usuario

    client_socket.close()  # finaliza a conexão


if __name__ == '__main__':
    cliente_banco()
