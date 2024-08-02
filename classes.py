class Pessoas:
    def __init__(self, nome, sobrenome, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco

class Medico(Pessoas):
    def __init__(self, nome, sobrenome, endereco, crm, especialidade):
        super().__init__(nome, sobrenome, endereco)
        self.crm = crm
        self.especialidade = especialidade
        self.nome = f"Dr. {self.nome}"  # Prefixar "Dr." ao nome

class Paciente(Pessoas):
    def __init__(self, nome, sobrenome, endereco, telefone):
        super().__init__(nome, sobrenome, endereco)
        self.telefone = telefone
