import socket

class Conta:
    cliente = 'Nome'
    rg = '12345678-90'
    senha = '123456'
    agencia = '0001'
    numero_conta = '1010-2'
    saldo = 0.00

def depositar(conta, valor):	
    conta.saldo += valor
    print(f'Depósito de R${valor:.2F} realizado')
    mostrar_saldo()

def sacar(conta, valor):	
    if valor <= conta.saldo:
        conta.saldo -= valor
        print(f'Saque de R${valor:.2F} realizado')
        mostrar_saldo()
    else:
        print('Saldo insuficiente.')

def transferir(conta, conta_destino, valor):	
    if valor <= conta.saldo:
        conta.saldo -= valor
        conta.extrato(-valor)
        print(f'Transferência de R${valor:.2F} realizada')
        mostrar_saldo()
    else:
        print('Saldo insuficiente.')
        
def menu(conta):
    print('-' * 30)
    print(f'     MENU DE OPERAÇÕES')
    print('-' * 30)
    print('Opções:')
    print('1 - Saldo')
    print('2 - Depósito')
    print('3 - Saque')
    print('4 - Transferência')
    print('5 - Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        mostrar_saldo(conta)
    elif opcao == '2':
        valor = float(input('Digite o valor a ser depositado: '))
        depositar(conta, valor)
    elif opcao == '3':
        valor = float(input('Digite o valor a ser sacado: '))
        sacar(conta, valor)
    elif opcao == '5':
        exit()

def mostrar_saldo(conta):
    print()
    print('-' * 40)
    print(f'CLIENTE - {conta.cliente}')
    print(f'AGÊNCIA {conta.agencia} CONTA {conta.numero_conta}')
    print(f'                        SALDO: R$ {conta.saldo:.2F}')
    print('-' * 40)
    aperte = input('Aperte ENTER para retornar ao MENU\nou (X e ENTER) para sair: ')
    if aperte == 'X' or aperte == 'x': 
        exit()
    else:
        menu()


def servidor_banco():
    # solicita o nome do host
    host = socket.gethostname()
    porta = 5001  # inicia a porta
    autenticacao = False

    server_socket = socket.socket()  # instância do socket

    server_socket.bind((host, porta))  # a função "bind" hospeda o endereço do host e da porta juntos

    # Configura quantos clientes o servidor pode escutar simultâenamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # aceita uma nova conexãõ
    print("Conectado com: " + str(address))
    while True:
        # recebe os dados. Não aceitará pacotes de dados maiores que 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # se não receber nenhum dado, termina
            break
        print("Mensagem recebida pelo usuario: " + str(data)) #Mostra no terminal o que foi recebido pelo cliente
        data = input(' -> ')
        conn.send(data.encode())  # envia dados para o cliente

    conn.close()  # Finaliza a conexão


if __name__ == '__main__':
    pessoa1 = Conta()
    pessoa1.cliente = 'Felipe Nascimento'
    pessoa1.rg = '12345678-90'
    pessoa1.numero_conta = '0001-1'
    pessoa1.saldo = 500.00
    
    pessoa2 = Conta()
    pessoa2.cliente = 'Icaro Brito'
    pessoa1.rg = '12345678-09'
    pessoa2.numero_conta = '0002-1'
    pessoa2.saldo = 500.00
    
    servidor_banco()
    

    while True:
        pessoa.menu()