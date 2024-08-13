from classes import Medico, Paciente
from variaveis import nome_data, sobrenome_data, endereco_data, crm_data, especialidade_data, telefone_data

def cadastro_medico(nome, sobrenome, endereco, crm, especialidade):
    nome_completo = "Dr. " + nome  # Adiciona "Dr." ao nome do médico
    novo_medico = Medico(nome_completo, sobrenome, endereco, crm, especialidade)
    nome_data.append(novo_medico.nome)
    sobrenome_data.append(novo_medico.sobrenome)
    endereco_data.append(novo_medico.endereco)
    crm_data.append(novo_medico.crm)
    especialidade_data.append(novo_medico.especialidade)

def cadastro_paciente(nome, sobrenome, endereco, telefone):
    novo_paciente = Paciente(nome, sobrenome, endereco, telefone)
    nome_data.append(novo_paciente.nome)
    sobrenome_data.append(novo_paciente.sobrenome)
    endereco_data.append(novo_paciente.endereco)
    telefone_data.append(novo_paciente.telefone)
