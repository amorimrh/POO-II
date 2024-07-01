from datetime import datetime
from departamento import Departamento
from projeto import Projeto
from reuniao import Reuniao
from pessoa import Funcionario, FuncionarioImpl

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.departamentos = []
        self.projetos = []
        self.reunioes = []

    def demitir_funcionario(self, nome):
        funcionario = self.buscar_funcionario(nome)
        if funcionario:
            self.funcionarios.remove(funcionario)
            for departamento in self.departamentos:
                if funcionario in departamento.funcionarios:
                    departamento.funcionarios.remove(funcionario)
            print(f"{nome} foi desligado(a) da empresa.")
        else:
            print("Funcionário Inexistente.")

    def adicionar_funcionario(self, funcionario, nome_departamento):
        departamento_encontrado = self.buscar_departamento(nome_departamento)
        if not departamento_encontrado:
            print(f"Erro: Departamento {nome_departamento} não encontrado. Funcionário {funcionario.nome} não foi adicionado à empresa.")
            return False

        if funcionario in self.funcionarios:
            print(f"Erro: Funcionário {funcionario.nome} já está registrado na empresa.")
            return False
        
        self.funcionarios.append(funcionario)

        if not departamento_encontrado.adicionar_funcionario(funcionario):
            self.funcionarios.remove(funcionario)
            print(f"Erro ao adicionar funcionário {funcionario.nome} ao departamento {nome_departamento}.")
            return False

        if isinstance(funcionario, FuncionarioImpl):
            funcionario.associar_departamento(departamento_encontrado)
        
        print(f"Funcionário {funcionario.nome} adicionado ao departamento {departamento_encontrado.nome} com sucesso.")
        return True

    def listar_funcionarios(self):
        if not self.funcionarios:
            return None
        return [funcionario.exibir_informacoes() for funcionario in self.funcionarios]

    def listar_funcionarios_ferias(self):
        hoje = datetime.now().strftime("%Y-%m-%d")
        return [funcionario.exibir_informacoes() for funcionario in self.funcionarios if funcionario.esta_de_ferias(hoje)]

    def listar_funcionarios_licenca(self):
        return [funcionario.exibir_informacoes() for funcionario in self.funcionarios if funcionario.esta_de_licenca()]

    def adicionar_departamento(self, nome):
        self.departamentos.append(Departamento(nome))

    def listar_departamentos(self):
        return [departamento.nome for departamento in self.departamentos]
    
    def buscar_departamento(self, nome_departamento):
        for departamento in self.departamentos:
            if departamento.nome == nome_departamento:
                return departamento
        return None

    def buscar_departamento_de_funcionario(self, nome_funcionario):
        for departamento in self.departamentos:
            for funcionario in departamento.funcionarios:
                if funcionario.nome == nome_funcionario:
                    return departamento.nome
        return None

    def buscar_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                return funcionario
        return None

    def adicionar_funcionario_em_ferias(self, nome, inicio, fim):
        funcionario = self.buscar_funcionario(nome)
        if funcionario:
            if funcionario.agendar_ferias(inicio, fim):
                print(f"Férias agendadas para o funcionário {nome} de {inicio} a {fim}.")
            else:
                print(f"Não foi possível agendar férias para o funcionário {nome} neste período.")
        else:
            print("Funcionário Inexistente.")

    def adicionar_funcionario_em_licenca(self, nome):
        funcionario = self.buscar_funcionario(nome)
        if funcionario:
            funcionario.solicitar_licenca()
            print(f"{nome} está agora de licença.")
        else:
            print("Funcionário Inexistente.")

    def alterar_funcionario(self, nome, cargo=None, salario=None, nome_departamento=None):
        funcionario = self.buscar_funcionario(nome)
        if funcionario:
            if cargo:
                if isinstance(funcionario, FuncionarioImpl):
                    funcionario.mudar_profissao(cargo)
                else:
                    print(f"Funcionário {nome} não pode mudar de profissão.")
            if salario:
                if isinstance(funcionario, FuncionarioImpl):
                    funcionario.mudar_salario(salario)
                else:
                    print(f"Funcionário {nome} não pode mudar de salário.")
            if nome_departamento:
                departamento = self.buscar_departamento(nome_departamento)
                if departamento:
                    if isinstance(funcionario, FuncionarioImpl):
                        funcionario.associar_departamento(departamento)
                    if funcionario not in departamento.funcionarios:
                        departamento.adicionar_funcionario(funcionario)
                    print(f"{nome} agora pertence ao departamento {nome_departamento}.")
                else:
                    print(f"Departamento {nome_departamento} não encontrado.")
            print(f"Dados alterados com sucesso para o funcionário {nome}.")
        else:
            print("Funcionário Inexistente.")

    def solicitar_reuniao(self, data, hora, assunto):
        reuniao = Reuniao(data, hora, assunto)
        self.reunioes.append(reuniao)
        print(f"Reunião solicitada para {data} às {hora} - {assunto}")

    def adicionar_projeto(self, nome):
        projeto = Projeto(nome)
        self.projetos.append(projeto)
        print(f"Projeto {nome} adicionado com sucesso!")

    def listar_projetos(self):
        return [projeto.nome for projeto in self.projetos]
