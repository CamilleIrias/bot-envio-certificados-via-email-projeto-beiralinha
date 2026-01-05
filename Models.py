class Curso:
    def __init__(self, nome, caminho):
        self.nome = nome
        self.caminho = caminho

class Aluno:
    def __init__(self, nome, emails):
        self.nome = nome
        self.emails = emails
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)