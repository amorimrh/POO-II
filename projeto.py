class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, funcionario):
        self.membros.append(funcionario)

    def listar_membros(self):
        return [membro.exibir_informacoes() for membro in self.membros]
