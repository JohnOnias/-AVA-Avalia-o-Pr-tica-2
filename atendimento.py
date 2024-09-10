# classe Medico com atributos nome e crm
class Medico:
    def __init__(self, nome=None, crm=None):
        self.nome = nome
        self.crm = crm


# classe Paciente com vários atributos pessoais
class Paciente:
    def __init__(self, nome=None, cpf=None, telefone=None, numero=None, rua=None, bairro=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.numero = numero
        self.rua = rua
        self.bairro = bairro


# classe Atendimento cria uma especie de relacao Medico/paciente
class Atendimento:
    def __init__(self, medico=None, paciente=None, data_do_atendimento=None):
        self.medico = medico
        self.paciente = paciente
        self.data_do_atendimento = data_do_atendimento


# adicionar lista telefônica
def adicionar_telefone():
    lista_telefone = []
    qtd = int(input("Digite quantos telefones quer adicionar: "))
    for i in range(qtd):
        telefone = input(f"Digite o numero telefônico {i + 1}: ")
        lista_telefone.append(telefone)
    
    return lista_telefone

# cadastra um médico e retorna o objeto Médico criado
def cadastro_medico():
    print("############# CADASTRO DO MÉDICO ##########")
    nome = input("Digite o nome do medico: ")
    crm = input("Digite o crm do médico: ")


    return Medico(nome, crm)  # Cria e retorna um objeto Medico


# cadastrar um paciente e retorna o objeto Paciente criado
def cadastro_paciente():
    print("############ CADASTRO DO PACIENTE ##########")
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o cpf do paciente: ")
    lista_telefone = adicionar_telefone()
    rua = input("Digite o nome da rua: ")
    numero = input("Digite o numero da casa: ")
    bairro = input("Digite o nome do bairro: ")


    return Paciente(nome, cpf, lista_telefone, numero, rua, bairro)


#criar um atendimento e retorna o objeto Atendimento criado
def salvar_atendimento(medico, paciente, data_do_atendimento):

    return Atendimento(medico, paciente, data_do_atendimento)


# mostra todos os atendimentos na lista
def mostrar_atendimento(lista_atendimento):
    for atendimento in lista_atendimento:
        print(f"############## ATENDIMENTO  DO DIA {atendimento.data_do_atendimento} ############### ")
        print("------------------------------------------------")
        print("DADOS DO MÉDICO")
        print(f"Nome: {atendimento.medico.nome}")
        print(f"CRM: {atendimento.medico.crm}")
        print("-------------------------------------------------")
        print("DADOS DO PACIENTE")
        print(f"Nome: {atendimento.paciente.nome}")
        print(f"CPF: {atendimento.paciente.cpf}")
        print(f"Rua: {atendimento.paciente.rua}")
        print(f"Numero: {atendimento.paciente.numero}")
        print(f"Bairro: {atendimento.paciente.bairro}")
        print(f"Telefones: {atendimento.paciente.telefone}")
        print("--------------------------------------------------")
        print("\n")


# filtra um médico da lista baseado no CRM
def filtrar_medico(crm, lista_medico):
    for medico in lista_medico:
        if medico.crm == crm:
            return medico
    return None


#filtra um paciente da lista baseado no CPF
def filtrar_paciente(cpf, lista_paciente):
    for paciente in lista_paciente:
        if paciente.cpf == cpf:
            return paciente
    return None



#busca e mostra os atendimentos de um médico específico baseado no CRM
def buscar_atendimento(crm, lista_atendimento):
    for atendimento in lista_atendimento:
        if atendimento.medico.crm == crm:
            print(f"############## ATENDIMENTO  DO DIA {atendimento.data_do_atendimento} ############### ")
            print("-------------------------------------------------")
            print("DADOS DO PACIENTE")
            print(f"Nome: {atendimento.paciente.nome}")
            print(f"CPF: {atendimento.paciente.cpf}")
            print(f"Rua: {atendimento.paciente.rua}")
            print(f"Numero: {atendimento.paciente.numero}")
            print(f"Bairro: {atendimento.paciente.bairro}")
            print(f"Telefones: {atendimento.paciente.telefone}")
            print("--------------------------------------------------")
            print("\n")



opt = 0
lista_atendimento = []
lista_medico = []
lista_paciente = []
medico = None
paciente = None

# Loop principal do menu
while opt != -1:
    print('-' * 40)
    print("[1] - Cadastrar Médico")
    print("[2] - Cadastrar Paciente")
    print("[3] - Salvar Atendimento")
    print("[4] - Mostrar todos os atendimentos")
    print("[5] - Buscar atendimento")
    print("[-1] - Encerrar")
    opt = int(input("Escolha: "))

    match opt:
        case 1:
            medico = cadastro_medico()
            lista_medico.append(medico)
        case 2:
            paciente = cadastro_paciente()
            lista_paciente.append(paciente)
        case 3:
            crm = input("Informe o crm do médico: ")
            cpf = input("Digite o cpf do paciente: ")

            filtro_paciente = filtrar_paciente(cpf, lista_paciente)
            filtro_medico = filtrar_medico(crm, lista_medico)

            if filtro_medico and filtro_paciente:
                data = input("Informe a data (dd/mm/aaaa): ")
                atendimento = salvar_atendimento(filtro_medico, filtro_paciente, data)
                lista_atendimento.append(atendimento)
            else:
                print("Médico ou paciente não existe")
        case 4:
            mostrar_atendimento(lista_atendimento)
        case 5:
            crm = input("Digite o crm do médico: ")
            buscar_atendimento(crm, lista_atendimento)
