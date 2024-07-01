class Reuniao:
    def __init__(self, data, hora, assunto):
        self.data = data
        self.hora = hora
        self.assunto = assunto

    def exibir_informacoes(self):
        return f"Data: {self.data}, Hora: {self.hora}, Assunto: {self.assunto}"
