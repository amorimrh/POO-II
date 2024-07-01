from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def exibir_informacoes(self):
        raise NotImplementedError("Método 'exibir_informacoes' deve ser implementado nas subclasses.")

class Funcionario(Pessoa, ABC):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome)
        self.cargo = cargo
        self.salario = salario
        self.ferias_agendadas = []
        self.licenca = False

    def agendar_ferias(self, inicio, fim):
        try:
            inicio = datetime.strptime(inicio, "%Y-%m-%d")
            fim = datetime.strptime(fim, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de data inválido. Use 'YYYY-MM-DD'.")

        if inicio >= fim:
            raise ValueError("A data de início das férias deve ser anterior à data de término.")

        conflito = any(inicio.date() <= periodo[1].date() and fim.date() >= periodo[0].date() for periodo in self.ferias_agendadas)
        if not conflito:
            self.ferias_agendadas.append((inicio, fim))
            return True
        return False

    def solicitar_licenca(self):
        self.licenca = True

    def esta_de_ferias(self, data=None):
        if not data:
            data = datetime.now().date()
        else:
            data = datetime.strptime(data, "%Y-%m-%d").date()
        for periodo in self.ferias_agendadas:
            inicio = periodo[0].date()
            fim = periodo[1].date()
            if inicio <= data <= fim:
                return True
        return False

    def esta_de_licenca(self):
        return self.licenca

    def calcular_descontos(self):
        if self.esta_de_licenca():
            desconto_percentual = 15
        elif self.esta_de_ferias():
            desconto_percentual = 10
        else:
            desconto_percentual = 5

        desconto_valor = (desconto_percentual / 100) * self.salario
        return desconto_percentual, desconto_valor

    def criar_holerite(self, mes, ano):
        hoje = datetime.now().strftime("%Y-%m-%d")
        descontos_percentual, descontos_valor = self.calcular_descontos()
        salario_base = self.salario

        holerite = {
            "Nome": self.nome,
            "Cargo": self.cargo,
            "Salário": f"R${salario_base:.2f}",
            "Mês": mes,
            "Ano": ano,
            "Está de férias": "Sim" if self.esta_de_ferias(hoje) else "Não",
            "Está de licença": "Sim" if self.esta_de_licenca() else "Não",
            "Descontos (% do salário base)": f"{descontos_percentual}%",
            "Descontos": descontos_valor,
            "Salário Líquido": salario_base - descontos_valor
        }
        return holerite

    def exibir_informacoes(self):
        info = f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"
        return info

class FuncionarioImpl(Funcionario):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome, cargo, salario)
        self.holerites = []
        self.departamento = None

    def mudar_profissao(self, novo_cargo):
        self.cargo = novo_cargo

    def associar_departamento(self, departamento):
        self.departamento = departamento

    def exibir_informacoes(self):
        info = super().exibir_informacoes()
        if self.departamento:
            info += f", Departamento: {self.departamento.nome}"
        return info

    def mudar_salario(self, novo_salario):
        self.salario = novo_salario
        print(f"Salário de {self.nome} alterado para R${novo_salario:.2f}")

    def criar_holerite(self, mes, ano):
        holerite = super().criar_holerite(mes, ano)
        self.holerites.append(holerite)
        return holerite

    def solicitar_treinamento(self, nivel, nome_treinamento, data_treinamento):
        print(f"{self.nome} solicitou treinamento de {nivel}: {nome_treinamento}, data {data_treinamento}")
