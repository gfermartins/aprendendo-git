from variaveis import crm_data, nome_data, especialidade_data

def consultar_medico(pesquisa):
    encontrados = []
    for i, nome in enumerate(nome_data):
        if pesquisa.lower() in nome.lower() or pesquisa.lower() in especialidade_data[i].lower():
            encontrado = {
                'crm': crm_data[i],
                'nome': nome_data[i],
                'especialidade': especialidade_data[i]
            }
            encontrados.append(encontrado)
    return encontrados