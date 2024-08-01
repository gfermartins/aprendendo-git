from medico import Medico
from variaveis import crm_data, nome_data, especialidade_data

def cadastro_medico(crm, nome, especialidade):
    novo_medico = Medico(crm, nome, especialidade)
    crm_data.append(novo_medico.crm)
    nome_data.append(novo_medico.nome)
    especialidade_data.append(novo_medico.especialidade)
    return novo_medico