from empresa import Empresa
from pessoa import FuncionarioImpl

def menu():
    print("\n*** Gestão Empresarial ***")
    print("1. Contratar Funcionário")
    print("2. Listar Funcionários")
    print("3. Agendar Treinamento")
    print("4. Alterar Funcionário")
    print("5. Listar Funcionários de Licença")
    print("6. Listar Funcionários em Férias")
    print("7. Adicionar Funcionário em Férias")
    print("8. Adicionar Funcionários de Licença")
    print("9. Solicitar Reunião")
    print("10. Listar Projetos")
    print("11. Adicionar Projeto")
    print("12. Listar Departamentos")
    print("13. Adicionar Departamento")
    print("14. Gerar Holerite")
    print("15. Demitir Funcionário")
    print("0. Sair")

def main():
    empresa = Empresa("Minha Empresa")

    empresa.adicionar_departamento("Suporte TI")
    empresa.adicionar_departamento("Administração")
    empresa.adicionar_departamento("Vendas")
    empresa.adicionar_departamento("Presidência")

    maria = FuncionarioImpl("Maria", "Analista Pleno", 5000)
    alicia = FuncionarioImpl("Alicia", "Psicóloga", 10000)
    joao = FuncionarioImpl("João", "Programador Pleno", 6000)
    ana = FuncionarioImpl("Ana", "Gerente", 8000)
    jose = FuncionarioImpl("José", "CEO", 30000)
    ricardo = FuncionarioImpl("Ricardo", "Suporte Senior", 9600)

    empresa.adicionar_funcionario(maria, "Suporte TI")
    empresa.adicionar_funcionario(alicia, "Administração")
    empresa.adicionar_funcionario(joao, "Vendas")
    empresa.adicionar_funcionario(ana, "Administração")
    empresa.adicionar_funcionario(jose, "Presidência")
    empresa.adicionar_funcionario(ricardo, "Suporte TI")

    empresa.adicionar_projeto("Angus")

    inicio_ferias_maria = "2024-06-05"
    fim_ferias_maria = "2024-07-15"
    empresa.adicionar_funcionario_em_ferias("Maria", inicio_ferias_maria, fim_ferias_maria)

    empresa.adicionar_funcionario_em_licenca("Ana")

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            nome_departamento = input("Nome do departamento: ")
            funcionario = FuncionarioImpl(nome, cargo, salario)
            if empresa.adicionar_funcionario(funcionario, nome_departamento):
                print(f"Funcionário {nome} adicionado com sucesso!")

        elif escolha == "2":
            print("\nFuncionários:")
            funcionarios = empresa.listar_funcionarios()
            if funcionarios:
                for funcionario in funcionarios:
                    print(funcionario)
            else:
                print("Nenhum funcionário cadastrado.")

        elif escolha == "3":
            nome = input("Nome do funcionário para treinamento: ")
            nivel = input("Nível do treinamento: ")
            nome_treinamento = input("Nome do treinamento: ")
            data_treinamento = input("Data do treinamento (YYYY-MM-DD): ")
            funcionario = empresa.buscar_funcionario(nome)
            if funcionario:
                funcionario.solicitar_treinamento(nivel, nome_treinamento, data_treinamento)
            else:
                print("Funcionário não encontrado.")

        elif escolha == "4":
            nome = input("Nome do funcionário: ")
            cargo = input("Novo cargo (deixe em branco para manter o atual): ")
            salario = float(input("Novo salário (deixe 0 para manter o atual): "))
            nome_departamento = input("Novo departamento (deixe em branco para manter o atual): ")
            empresa.alterar_funcionario(nome, cargo, salario if salario != 0 else None, nome_departamento)

        elif escolha == "5":
            print("\nFuncionários de Licença:")
            funcionarios_licenca = empresa.listar_funcionarios_licenca()
            if funcionarios_licenca:
                for funcionario in funcionarios_licenca:
                    print(funcionario)
            else:
                print("Nenhum funcionário em licença.")

        elif escolha == "6":
            print("\nFuncionários em Férias:")
            funcionarios_ferias = empresa.listar_funcionarios_ferias()
            if funcionarios_ferias:
                for funcionario in funcionarios_ferias:
                    print(funcionario)
            else:
                print("Nenhum funcionário de férias.")

        elif escolha == "7":
            nome = input("Nome do funcionário: ")
            inicio = input("Data de início das férias (YYYY-MM-DD): ")
            fim = input("Data de término das férias (YYYY-MM-DD): ")
            empresa.adicionar_funcionario_em_ferias(nome, inicio, fim)

        elif escolha == "8":
            nome = input("Nome do funcionário para licença: ")
            empresa.adicionar_funcionario_em_licenca(nome)

        elif escolha == "9":
            data = input("Data da reunião (YYYY-MM-DD): ")
            hora = input("Hora da reunião (HH:MM): ")
            assunto = input("Assunto da reunião: ")
            empresa.solicitar_reuniao(data, hora, assunto)

        elif escolha == "10":
            print("\nProjetos:")
            projetos = empresa.listar_projetos()
            if projetos:
                for projeto in projetos:
                    print(projeto)
            else:
                print("Nenhum projeto cadastrado.")

        elif escolha == "11":
            nome_projeto = input("Nome do projeto: ")
            empresa.adicionar_projeto(nome_projeto)

        elif escolha == "12":
            print("\nDepartamentos:")
            departamentos = empresa.listar_departamentos()
            if departamentos:
                for departamento in departamentos:
                    print(departamento)
            else:
                print("Nenhum departamento cadastrado.")

        elif escolha == "13":
            nome_departamento = input("Nome do departamento: ")
            empresa.adicionar_departamento(nome_departamento)

        elif escolha == "14":
            nome_funcionario = input("Nome do funcionário para gerar holerite: ")
            mes = input("Mês do holerite (MM): ")
            ano = input("Ano do holerite (YYYY): ")
            funcionario = empresa.buscar_funcionario(nome_funcionario)
            if funcionario:
                holerite = funcionario.criar_holerite(mes, ano)
                print("\nHolerite Gerado:")
                for chave, valor in holerite.items():
                    print(f"{chave}: {valor}")
            else:
                print("Funcionário não encontrado.")

        elif escolha == "15":
            nome = input("Nome do funcionário para demissão: ")
            empresa.demitir_funcionario(nome)

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
