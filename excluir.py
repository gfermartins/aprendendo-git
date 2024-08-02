from variaveis import nome_data, sobrenome_data, endereco_data, crm_data, especialidade_data, telefone_data

def excluir_pessoa(indice):
    if 0 <= indice < len(nome_data):
        del nome_data[indice]
        del sobrenome_data[indice]
        del endereco_data[indice]
        if indice < len(crm_data):
            del crm_data[indice]
        if indice < len(especialidade_data):
            del especialidade_data[indice]
        if indice < len(telefone_data):
            del telefone_data[indice]
        return True
    return False