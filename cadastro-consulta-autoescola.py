class Pessoa():

    def __init__(self, nome, idade, cpf, matricula, servico):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.matricula = matricula
        self.servico = servico


class Alunos(Pessoa):

    def __init__(self, nome, idade, cpf, matricula, servico, categoria):
        super().__init__(nome, idade, cpf, matricula, servico)
        self.categoria = categoria

    def imprimir_cadastro():
        print('Aluno: ', new_cad.nome,
              '\nIdade: ', new_cad.idade,
              '\nCPF:', new_cad.cpf,
              '\nMatrícula:', new_cad.matricula,
              '\nServiço: ', new_cad.servico,
              '\nCategoria:', new_cad.categoria.upper())


class Instrutores(Pessoa):

    def __init__(self, nome, idade, cpf, matricula, servico, categoria, habilitacao, certificacao):
        super().__init__(nome, idade, cpf, matricula,servico)
        self.habilitacao = habilitacao
        self.certificacao = certificacao
        self.categoria = categoria

    def imprimir_cadastro():
        print('Instrutores: ', new_cad.nome,
              '\nIdade:', new_cad.idade,
              '\nCPF:', new_cad.cpf,
              '\nMatrícula:', new_cad.matricula,
              '\nHabilitação: ', new_cad.habilitacao,
              '\nCertificação:', new_cad.certificacao,
              '\nCategoria:', new_cad.categoria.upper())


class Veiculos():

    def __init__(self, moto='Moto CG 125', carro='Fiat UNO 1.0', caminhao='Scania R450',
                 onibus='Mercedes Benz Sprinter'):
        self.moto = moto
        self.carro = carro
        self.caminhao = caminhao
        self.onibus = onibus


##class Categorias():

    ##def __init__(self, tipo):
        ##self.tipo = tipo


# Inicio da Execução

import random as rand

print('Seja bem-vindo a Auto Escola UniAteneu...')
while (True):
    init_cad = input('Vamos iniciar o seu cadastro? S - Sim / N - Não --> ')

    if init_cad.upper() == 'S':
        init_cad = input('Vamos cadastrar Aluno ou Instrutor? A - Aluno / I - Instrutor --> ')
        if init_cad.upper() == 'A':
            new_cad = Alunos(
            input('Qual o seu nome? '),  # nome
            input('Quantos anos você tem? '),  # idade
            input('Qual o seu CPF? '),  # cpf
            input('Qual a sua matricula? '),  # matricula
            input('<<Escolha um serviço >>'
                  '\nPH - Primeira habilitação'
                  '\nRN - Renovação'
                  '\nIN - Inclusão de nova categoria'
                  '\nAP - Aulas Práticas'
                  '\nQual serviço você deseja?: '),  # serviço
            input('Para qual categoria você deseja atendimento? ')  # categoria
             )
        elif init_cad.upper() == 'I':
            new_cad = Instrutores(
            input('Qual o seu nome? '),  # nome
            input('Qual a sua idade? '),  # idade
            input('Qual o seu CPF? '),  # cpf
            input('Qual a sua matricula? '),# matricula
            "",
            input('Será instrutor de qual categoria'),  # categoria
            input('Qual sua habilitação?'), # habilitação
            input('Quais suas certificações?'),  # certificação
            )
        new_cad.idade = new_cad.idade + " anos"
        new_cad.cpf = new_cad.cpf[:3] + "." + new_cad.cpf[3:6] + "." + new_cad.cpf[6:9] + "-" + new_cad.cpf[9:]
        break
    elif init_cad.upper() == 'N':
        cad_exis = input('Você já tem cadastro no nosso sistema? S - Sim / N - Não --> ')
        if cad_exis.upper() == 'S':
            print('você já possui cadastro')
            break
        elif cad_exis.upper() == 'N':
            print('você será redirecionado para o cadastro')
        else:
            continue
    else:
        print("digite uma opção valida")
if new_cad.servico.upper() == 'PH':
    new_cad.servico = 'Primeira Habilitação'
    new_cad.matricula = round(rand.random() * 100000)
elif new_cad.servico.upper() == 'RN':
    print()
elif new_cad.servico.upper() == 'IN':
    print()
elif new_cad.servico.upper() == 'AP':
    print()
elif new_cad.servico.upper() == 'CI':
    print()
else:
    print("digite uma opção valida")

if new_cad.categoria.upper() == 'A':
    veiculo = Veiculos().moto
elif new_cad.categoria.upper() == 'B':
    veiculo = Veiculos().carro
    
elif new_cad.categoria.upper() == 'D':
    veiculo = Veiculos().onibus
elif new_cad.categoria.upper() == 'E':
    veiculo = Veiculos().caminhao

Alunos.imprimir_cadastro()
print('\nO veículo designado será: ', veiculo)

Instrutores.imprimir_cadastro()
print('\nCadastro realizado com sucesso!')