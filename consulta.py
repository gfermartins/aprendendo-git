from variaveis import nome_data, sobrenome_data, endereco_data, crm_data, especialidade_data, telefone_data

def consultar_medicos(pesquisa):
    encontrados = []
    for i in range(len(nome_data)):
        if (pesquisa.lower() in nome_data[i].lower() or 
            pesquisa.lower() in sobrenome_data[i].lower() or 
            (i < len(especialidade_data) and pesquisa.lower() in especialidade_data[i].lower())):
            
            if i < len(crm_data):  # Verifica se é um médico
                encontrado = {
                    'nome': nome_data[i],
                    'sobrenome': sobrenome_data[i],
                    'endereco': endereco_data[i],
                    'crm': crm_data[i],
                    'especialidade': especialidade_data[i]
                }
                encontrados.append(encontrado)
    return encontrados

def consultar_pacientes(pesquisa):
    encontrados = []
    for i in range(len(nome_data)):
        if (pesquisa.lower() in nome_data[i].lower() or 
            pesquisa.lower() in sobrenome_data[i].lower()):
            
            if i < len(telefone_data):  # Verifica se é um paciente
                encontrado = {
                    'nome': nome_data[i],
                    'sobrenome': sobrenome_data[i],
                    'endereco': endereco_data[i],
                    'telefone': telefone_data[i]
                }
                encontrados.append(encontrado)
    return encontrados
