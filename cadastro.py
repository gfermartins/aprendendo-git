from classes import Medico, Paciente
from variaveis import crm_data, nome_data, especialidade_data, sobrenome_data, endereco_data, telefone_data

def cadastro_medico(nome, sobrenome, endereco, crm, especialidade):
    novo_medico = Medico(nome, sobrenome, endereco, crm, especialidade)
    crm_data.append(novo_medico.crm)
    nome_data.append(novo_medico.nome)
    especialidade_data.append(novo_medico.especialidade)
    sobrenome_data.append(novo_medico.sobrenome)
    endereco_data.append(novo_medico.endereco)
    return novo_medico

def cadastro_paciente(nome, sobrenome, endereco, telefone):
    novo_paciente = Paciente(nome, sobrenome, endereco, telefone)
    nome_data.append(novo_paciente.nome)
    sobrenome_data.append(novo_paciente.sobrenome)
    endereco_data.append(novo_paciente.endereco)
    telefone_data.append(novo_paciente.telefone)
    return novo_paciente
