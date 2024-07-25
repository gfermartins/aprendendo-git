from variaveis import crm_data, nome_data, especialidade_data

def excluir_medico(indice):
    if 0 <= indice < len(nome_data):
        del crm_data[indice]
        del nome_data[indice]
        del especialidade_data[indice]
        return True
    return False