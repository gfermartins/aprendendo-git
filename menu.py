from cadastro import cadastro_medico
from consulta import consultar_medico
from excluir import excluir_medico
from variaveis import crm_data, nome_data, especialidade_data

def menu():
    while True:
        opcao = int(input('1 - Cadastrar médicos\n2 - Consultar médicos\n3 - Excluir médicos\n4 - Sair\n'))
        
        if opcao == 1:
            while True:
                crm = input('Digite o CRM do médico que deseja cadastrar: ')
                nome = input('Digite o nome do médico que deseja cadastrar: ')
                especialidade = input('Digite a especialidade do médico que deseja cadastrar: ')
                
                novo_medico = cadastro_medico(crm, nome, especialidade)
                crm_data.append(novo_medico['crm'])
                nome_data.append(novo_medico['nome'])
                especialidade_data.append(novo_medico['especialidade'])
                
                print('Médicos cadastrados:')
                print(nome_data, crm_data, especialidade_data)
                
                continuar = input('Deseja continuar cadastrando médicos? S/N: ')
                if continuar.upper() != 'S':
                    break

        elif opcao == 2:
            while True:
                pesquisa = input('Digite o nome ou a especialidade do médico que deseja pesquisar: ')
                resultados = consultar_medico(pesquisa)
                
                if resultados:
                    for resultado in resultados:
                        print(f"CRM: {resultado['crm']}, Nome: {resultado['nome']}, Especialidade: {resultado['especialidade']}")
                else:
                    print('Nenhum médico encontrado.')
                
                continuar = input('Deseja fazer uma nova consulta? S/N: ')
                if continuar.upper() != 'S':
                    break

        elif opcao == 3:
            while True:
                print('Médicos cadastrados:')
                for i, nome in enumerate(nome_data):
                    print(f"{i} - Nome: {nome}, CRM: {crm_data[i]}, Especialidade: {especialidade_data[i]}")
                
                try:
                    num_medico = int(input('Qual médico você deseja excluir? Digite o número correspondente: '))
                    if excluir_medico(num_medico):
                        print('Médico excluído com sucesso.')
                    else:
                        print('Número de médico inválido.')
                except ValueError:
                    print('Entrada inválida. Por favor, digite um número.')

                continuar = input('Deseja continuar excluindo médicos? S/N: ')
                if continuar.upper() != 'S':
                    break

        elif opcao == 4:
            print('Saindo...')
            break

        else:
            print('Você selecionou uma opção inválida!')

if __name__ == '__main__':
    menu()
#segundo commit