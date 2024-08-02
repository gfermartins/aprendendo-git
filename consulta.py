from variaveis import nome_data, sobrenome_data, endereco_data, crm_data, especialidade_data, telefone_data

def consultar_pessoas(pesquisa):
    encontrados = []
    for i, nome in enumerate(nome_data):
        if pesquisa.lower() in nome.lower() or pesquisa.lower() in especialidade_data[i].lower() or pesquisa.lower() in sobrenome_data[i].lower():
            encontrado = {
                'nome': nome_data[i],
                'sobrenome': sobrenome_data[i],
                'endereco': endereco_data[i],
                'crm': crm_data[i] if i < len(crm_data) else '',
                'especialidade': especialidade_data[i] if i < len(especialidade_data) else '',
                'telefone': telefone_data[i] if i < len(telefone_data) else ''
            }
            encontrados.append(encontrado)
    return encontrados