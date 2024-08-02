from cadastro import cadastro_medico, cadastro_paciente
from consulta import consultar_pessoas
from excluir import excluir_pessoa
from variaveis import nome_data, sobrenome_data, endereco_data, crm_data, especialidade_data, telefone_data

def menu():
    while True:
        opcao = int(input('1 - Cadastrar médicos\n2 - Cadastrar pacientes\n3 - Consultar pessoas\n4 - Excluir pessoa\n5 - Sair\n'))
        
        if opcao == 1:
            while True:
                nome = input('Digite o nome do médico: ')
                sobrenome = input('Digite o sobrenome do médico: ')
                endereco = input('Digite o endereço do médico: ')
                crm = input('Digite o CRM do médico: ')
                especialidade = input('Digite a especialidade do médico: ')
                
                cadastro_medico(nome, sobrenome, endereco, crm, especialidade)
                
                print('Médicos cadastrados:')
                for i in range(len(nome_data)):
                    if i < len(crm_data):
                        print(f"Nome: {nome_data[i]}, Sobrenome: {sobrenome_data[i]}, Endereço: {endereco_data[i]}, CRM: {crm_data[i]}, Especialidade: {especialidade_data[i]}")
                
                continuar = input('Deseja continuar cadastrando médicos? S/N: ')
                if continuar.upper() != 'S':
                    break
        
        elif opcao == 2:
            while True:
                nome = input('Digite o nome do paciente: ')
                sobrenome = input('Digite o sobrenome do paciente: ')
                endereco = input('Digite o endereço do paciente: ')
                telefone = input('Digite o telefone do paciente: ')
                
                cadastro_paciente(nome, sobrenome, endereco, telefone)
                
                print('Pacientes cadastrados:')
                for i in range(len(nome_data)):
                    if i < len(telefone_data):
                        print(f"Nome: {nome_data[i]}, Sobrenome: {sobrenome_data[i]}, Endereço: {endereco_data[i]}, Telefone: {telefone_data[i]}")
                
                continuar = input('Deseja continuar cadastrando pacientes? S/N: ')
                if continuar.upper() != 'S':
                    break

        elif opcao == 3:
            while True:
                pesquisa = input('Digite o nome, sobrenome ou especialidade que deseja pesquisar: ')
                resultados = consultar_pessoas(pesquisa)
                
                if resultados:
                    for resultado in resultados:
                        print(f"Nome: {resultado['nome']}, Sobrenome: {resultado['sobrenome']}, Endereço: {resultado['endereco']}, CRM: {resultado['crm']}, Especialidade: {resultado['especialidade']}, Telefone: {resultado['telefone']}")
                else:
                    print('Nenhuma pessoa encontrada.')
                
                continuar = input('Deseja fazer uma nova consulta? S/N: ')
                if continuar.upper() != 'S':
                    break

        elif opcao == 4:
            while True:
                print('Pessoas cadastradas:')
                for i, nome in enumerate(nome_data):
                    print(f"{i} - Nome: {nome}, Sobrenome: {sobrenome_data[i]}, Endereço: {endereco_data[i]}, CRM: {crm_data[i] if i < len(crm_data) else ''}, Especialidade: {especialidade_data[i] if i < len(especialidade_data) else ''}, Telefone: {telefone_data[i] if i < len(telefone_data) else ''}")
                
                try:
                    num_pessoa = int(input('Qual pessoa você deseja excluir? Digite o número correspondente: '))
                    if excluir_pessoa(num_pessoa):
                        print('Pessoa excluída com sucesso.')
                    else:
                        print('Número de pessoa inválido.')
                except ValueError:
                    print('Entrada inválida. Por favor, digite um número.')

                continuar = input('Deseja continuar excluindo pessoas? S/N: ')
                if continuar.upper() != 'S':
                    break

        elif opcao == 5:
            print('Saindo...')
            break

        else:
            print('Você selecionou uma opção inválida!')

if __name__ == '__main__':
    menu()