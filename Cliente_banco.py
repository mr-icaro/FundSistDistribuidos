import socket


def cliente_banco():
    host = socket.gethostname()  # Recebe o nome do host, que também é usado pelo servidor por estarem ambos na mesma máquina
    port = 5001  #  Número da porta do servidor socket

    client_socket = socket.socket()  # Inicia a instância do socket
    client_socket.connect((host, port))  # Conecta ao servidor

    message = 'iniciar'  # aguarda a entrada de dados

    while message.lower().strip() != 'finalizar': #se digitar finalizar, termina o programa para o cliente e o servidor tb
        client_socket.send(message.encode())  # envia a mensagem para o servidor
        data = client_socket.recv(1024).decode()  # recebe a resposta do servidor

        print('Recebido do servidor: ' + data)  # Mostra os dados recebidos no terminal

        if data == 'Encerrando...':
            client_socket.close()
            exit()

        message = input("")  # aguarda uma nova entrada de dados do usuario

    client_socket.close()  # finaliza a conexão


if __name__ == '__main__':
    cliente_banco()
