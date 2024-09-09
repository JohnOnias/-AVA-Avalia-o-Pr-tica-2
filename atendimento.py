
class Medico:
    nome:None
    crm: None

class Paciente:
    nome:None
    cpf:None
    telefone: None
    numero:None
    rua:None
    bairro:None

class Atendimento:
    medico:Medico
    paciente:Paciente
    data_atendimento: None


def cadastro_medico():
    print("############# CADASTRO DO MÉDICO ##########")
    medico = Medico()
    medico.nome = input("Digite o nome: ")
    medico.crm = input("Digite o crm do médico: ")
    
    return medico

def cadastro_paciente():
    print("############ CADASTRO DO PACIENTE ##########")
    paciente = Paciente()
    paciente.nome = input("Digite o nome do paciente: ")
    paciente.cpf = input("Digite o cpf do paciente: ")
    paciente.telefone = input("Digite o telefone do paciente: ")
    paciente.numero = input("Digite o numero da rua: ")
    paciente.rua = input("Digite o nome da rua: ")
    paciente.bairro = input("Digite o nome do bairro: ")
    
    return paciente

def salvar_atendimento(medico, paciente, data):
    atendimento = Atendimento()
    atendimento.data = data
    atendimento.medico = medico
    atendimento.paciente = paciente

    return atendimento

def mostrar_medicos(lista_medico):
    for lista in lista_medico:
       print(f"Nome: {lista.nome} | CRM: {lista.crm}")

def filtrar_medico(crm, lista_medico):
    for lista in lista_medico:
        if lista.crm == crm:
            return True

    return False


opt = 0
lista_atendimento = []
lista_medico = []
lista_paciente = []
medico = None
paciente = None

while opt != 5:
    print("[1] - Cadastrar Médico")
    print("[2] - Cadastrar Paciente")
    print("[3] - Cadastrar Salvar Atendimento")
    print("[4] - Mostrar todos os médicos: ")
    opt = int(input("Escolha: "))

    match opt:
        case 1:
            medico = cadastro_medico()
            lista_medico.append(medico)
        case 2:
            paciente = cadastro_paciente()
            lista_paciente.append(paciente)
        case 3:
            crm = input("Informe o crm do medico: ")
            if filtrar_medico(crm, lista_medico):
                data = input("Informe a data: ")
                atendimento = salvar_atendimento(medico, paciente, data)
                lista_atendimento.append(atendimento)
                print("Atendimento adicionado!")
            else:
                print("Medico não existe")
        case 4:
            mostrar_medicos(lista_medico)
        