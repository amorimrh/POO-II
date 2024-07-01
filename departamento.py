class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)
            return True
        return False

    def listar_funcionarios(self):
        return [funcionario.nome for funcionario in self.funcionarios if funcionario]

    def buscar_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                return funcionario
        return None
