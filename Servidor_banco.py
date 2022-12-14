import socket

class Conta:
    cliente = 'Nome'
    rg = '12345678-90'
    senha = '123456'
    agencia = '0001'
    numero_conta = '1010-2'
    saldo = 0.00

def depositar(conta, valor, conn):	
    conta.saldo += valor
    mensagem = f'Depósito de R${valor:.2F} realizado com sucesso.'
    conn.send(mensagem.encode())
    mostrar_saldo(conta, conn)

def sacar(conta, valor, conn):	
    if valor <= conta.saldo:
        conta.saldo -= valor
        mensagem = f'Saque de R${valor:.2F} realizado com sucesso.'
        conn.send(mensagem.encode())
        mensagem = 'Tecle ENTER para continuar'
        conn.send(mensagem.encode())
        mostrar_saldo(conta, conn)
    else:
        mensagem = 'Saldo insuficiente.'
        conn.send(mensagem.encode())
        menu(conta, conn)

def transferir(conta, conta_destino, valor, conn):	
    if valor <= conta.saldo:
        conta.saldo -= valor
        conta_destino.saldo += valor
        mensagem = f'Transferência de R${valor:.2F} realizada com sucesso.'
        conn.send(mensagem.encode())
        mostrar_saldo(conta, conn)
    else:
        mensagem = 'Saldo insuficiente.'
        conn.send(mensagem.encode())
        menu(conta, conn)
        
def menu(conta, conn):
    mensagem = ('\n\nMENU DE OPERAÇÕES\nOpções:\n1 - Saldo\n2 - Depósito\n3 - Saque\n4 - Transferência\n5 - Sair\n6 - Novo login\nDigite a opção desejada: ')
    conn.send(mensagem.encode())
    opcao = str(conn.recv(1024).decode())

    if opcao == '1':
        mostrar_saldo(conta, conn)

    elif opcao == '2':
        mensagem = ('Digite o valor a ser depositado: ')
        conn.send(mensagem.encode())
        valor = float(conn.recv(1024).decode())
        depositar(conta, valor, conn)

    elif opcao == '3':
        mensagem = ('Digite o valor a ser sacado: ')
        conn.send(mensagem.encode())
        valor = float(conn.recv(1024).decode())
        sacar(conta, valor, conn)

    elif opcao == '4':
        mensagem = ('Digite o valor que deseja transferir: ')
        conn.send(mensagem.encode())
        valor = float(conn.recv(1024).decode())
        mensagem = ('Digite a conta para qual deseja transferir: ')
        conn.send(mensagem.encode())
        conta_destino = str(conn.recv(1024).decode())
        beneficiario = ''

        if conta.numero_conta == conta_destino:
            mensagem = ('Não é possível transferir para sua própria conta.')
            conn.send(mensagem.encode())
            menu(conta, conn)
        else:
            if conta_destino == pessoa1.numero_conta:
                beneficiario = pessoa1.cliente
                cliente_destino = pessoa1
            else:
                beneficiario = pessoa2.cliente
                cliente_destino = pessoa2

            mensagem = (f'Nome do beneficiário: {beneficiario}. Tecle S para confirmar a operação, ou N para cancelar')
            conn.send(mensagem.encode())
            confirmacao = str(conn.recv(1024).decode())
            if confirmacao == 'S' or confirmacao == 's': 
                transferir(conta, cliente_destino, valor, conn)
            else:
                mensagem = ('\nOperação cancelada.\n')
                conn.send(mensagem.encode())
                menu(conta, conn)


    elif opcao == '5':
        mensagem = ('\nEncerrando...')
        conn.send(mensagem.encode())
        conn.close()
        exit()

    elif opcao =='6':
        mensagem = ('Insira seus dados para fazer um novo login')
        conn.send(mensagem.encode())
        fazer_login(conn, autenticacao=False)


def mostrar_saldo(conta, conn):
    mensagem = (f'\nCLIENTE: {conta.cliente} RG: {conta.rg}')
    conn.send(mensagem.encode())
    mensagem = (f'\nAGÊNCIA: {conta.agencia} CONTA: {conta.numero_conta}')
    conn.send(mensagem.encode())
    mensagem = (f'\nSALDO: R$ {conta.saldo:.2F}')
    conn.send(mensagem.encode())
    mensagem = ('\n' + ('-' * 40))
    conn.send(mensagem.encode())

    mensagem = '\nAperte M para retornar ao MENU\nou qualquer outra tecla para sair: '
    conn.send(mensagem.encode())
    aperte = str(conn.recv(1024).decode())
    if aperte == 'M' or aperte == 'm': 
        menu(conta, conn)
    else:
        mensagem = ('\nEncerrando...\n')
        conn.send(mensagem.encode())
        conn.close()
        exit()
        
def fazer_login(conn, autenticacao):
    while True:
        if autenticacao == False:
            mensagem = '\nDigite o número da sua conta: '
            conn.send(mensagem.encode())
            num_conta = str(conn.recv(1024).decode())
            if not num_conta:
                print("\nNenhuma mensagem recebida do usuario.\n")
                break

            mensagem = '\nDigite sua senha: '
            conn.send(mensagem.encode())
            senha = str(conn.recv(1024).decode())
            if not senha:
                print("\nNenhuma mensagem recebida do usuario.\n")
                break

            if num_conta == pessoa1.numero_conta:
                if senha == pessoa1.senha:
                    mensagem = '\nAutenticado com sucesso.'
                    conn.send(mensagem.encode())
                    autenticacao = True
                    menu(pessoa1, conn)
                else:
                    mensagem = '\nSenha incorreta.\n'
                    conn.send(mensagem.encode())
                    break

            elif num_conta == pessoa2.numero_conta:
                if senha == pessoa2.senha:
                    mensagem = '\nAutenticado com sucesso.'
                    conn.send(mensagem.encode())
                    autenticacao = True
                    menu(pessoa2, conn)
                else:
                    mensagem = '\nSenha incorreta.'
                    conn.send(mensagem.encode())
                    break


def servidor_banco():
    # solicita o nome do host
    host = socket.gethostname()
    porta = 5001  # inicia a porta
    autenticacao = False

    server_socket = socket.socket()  # instância do socket

    server_socket.bind((host, porta))  # A função "bind" hospeda o endereço do host e da porta juntos

    # Configura quantos clientes o servidor pode escutar simultâenamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # Aceita uma nova conexão
    print("Conectado com: " + str(address))
    autenticacao = False

    fazer_login(conn, autenticacao)

    conn.close()  # Finaliza a conexão


if __name__ == '__main__':
    pessoa1 = Conta()
    pessoa1.cliente = 'Felipe Nascimento'
    pessoa1.rg = '12345678-90'
    pessoa1.senha = '1234'
    pessoa1.numero_conta = '0001-1'
    pessoa1.saldo = 500.00
    
    pessoa2 = Conta()
    pessoa2.cliente = 'Icaro Brito'
    pessoa2.rg = '12345678-09'
    pessoa2.senha = '4321'
    pessoa2.numero_conta = '0002-1'
    pessoa2.saldo = 500.00
    
    servidor_banco()
