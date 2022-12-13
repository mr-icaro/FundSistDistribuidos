import socket


def servidor_banco():
    # solicita o nome do host
    host = socket.gethostname()
    porta = 5001  # inicia a porta

    server_socket = socket.socket()  # instância do socket

    server_socket.bind((host, porta))  # a função "bind" hospeda o endereço do host e da porta juntos

    # Configura quantos clientes o servidor pode escutar simultâenamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # aceita uma nova conexãõ
    print("Connection from: " + str(address))
    while True:
        # recebe os dados. Não aceitará pacotes de dados maiores que 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # se não receber nenhum dado, termina
            break
        print("Msg recebida pelo usuario: " + str(data)) #Mostra no terminal o que foi recebido pelo cliente
        data = input(' -> ')
        conn.send(data.encode())  # envia dados para o cliente

    conn.close()  # Finaliza a conexão


if __name__ == '__main__':
    servidor_banco()