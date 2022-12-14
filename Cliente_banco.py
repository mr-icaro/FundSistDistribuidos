# Universidade Federal da Bahia
# Disciplina: Fundamentos de Sistemas Distribuídos
# Professor: Raimundo Macêdo
# Projeto: Sistema Distribuído Simples para Manutenção de Contas Bancárias
# Desenvolvedores: Felipe Nascimento (felipern@ufba.br), e Icaro Brito (icarobss@ufba.br)
# 2022

# Importa biblioteca necessária para o funcionamento da comunicação
import socket

# Função que administra a conexão no lado do cliente,
# possibilita a troca de mensagens com o seridor
def cliente_banco():
    host = socket.gethostname()  # Recebe o nome do host, que também é usado pelo servidor por estarem ambos na mesma máquina
    port = 5001  # Número da porta do servidor socket

    client_socket = socket.socket()  # Cria a instância do socket
    client_socket.connect((host, port))  # Conecta ao servidor

    mensagem = ''  # Define a mensagem

    # Se digitar "finalizar", termina o programa para o cliente e o servidor
    while mensagem.lower().strip() != 'finalizar':
        data = client_socket.recv(1024).decode()  # Recebe a resposta do servidor

        # Mostra os dados recebidos do servidor no terminal
        print('Recebido do servidor: ' + data)

        # Se receber do servidor a resposta de encerramento da operação, finaliza o programa
        if data == 'Encerrando...':
            client_socket.close()
            exit()

        mensagem = input("")  # Aguarda uma nova entrada de dados do usuario
        client_socket.send(mensagem.encode())  # Envia a mensagem para o servidor

    client_socket.close()  # Finaliza a conexão


if __name__ == '__main__':
    # Chama a função principal para iniciar
    # a conexão do cliente com o servidor,
    # e solicitar as operações bancárias
    cliente_banco()
