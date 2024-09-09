
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

def mostrar_atendimento(lista_atendimento):
    for lista in lista_atendimento:
       print(f"############## ATENDIMENTO  DO DIA {lista.data} ############### ")
       
       print("------------------------------------------------")
       print("DADOS DO MÉDICO")
       print(f"Nome: {lista.medico.nome}")
       print(f"CRM: {lista.medico.crm}")
       print("-------------------------------------------------")
       
       print("\n")
       
       print("-------------------------------------------------")
       print("DADOS DO PACIENTE")
       print("Nome:",lista.paciente.nome)
       print("CPF:",lista.paciente.cpf)
       print("Rua:",lista.paciente.rua)
       print("--------------------------------------------------")

def filtrar_medico(crm, lista_medico):
    for index, lista in enumerate(lista_medico):
        if lista.crm == crm:
            return lista_medico[index]
        

    return None

def filtrar_paciente(cpf, lista_pacientes):
    for index, lista in enumerate(lista_pacientes):
        if lista.cpf == cpf:
            return lista_pacientes[index]

    return None

def buscar_atendimento(crm, lista_atendimento):
    for lista in lista_atendimento:
        if lista.medico.crm == crm:
                print(f"############## ATENDIMENTO  DO DIA {lista.data} ############### ")
                print("-------------------------------------------------")
                print("DADOS DO PACIENTE")
                print("Nome:",lista.paciente.nome)
                print("CPF:",lista.paciente.cpf)
                print("Rua:",lista.paciente.rua)
                print("--------------------------------------------------")
                print("\n")
            


opt = 0
lista_atendimento = []
lista_medico = []
lista_paciente = []
medico = None
paciente = None

while opt != -1:
    print("[1] - Cadastrar Médico")
    print("[2] - Cadastrar Paciente")
    print("[3] - Salvar Atendimento")
    print("[4] - Mostrar todos os atendimentos: ")
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
            crm = input("Informe o crm do medico: ")
            cpf = input("Digite o cpf do paciente: ")
            
            filtro_paciente = filtrar_paciente(cpf, lista_paciente)
            filtro_medico  =  filtrar_medico(crm, lista_medico)
            
            if filtro_medico and filtro_paciente:
                data = input("Informe a data: ")
                atendimento = salvar_atendimento(medico, paciente, data)
                lista_atendimento.append(atendimento)
            else:
                print("Medico ou paciente não existe")
        case 4:
            mostrar_atendimento(lista_atendimento)
        
        case 5:
            crm = input("Digite o crm do médico: ")
            buscar_atendimento(crm, lista_atendimento)
        
        