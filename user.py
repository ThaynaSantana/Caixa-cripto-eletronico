class User:

    def __init__(self, nome, password, cpf):
        self.nome = nome
        self.password = password
        self.cpf = cpf
        self.__ativo = True
    
    def desativar(self):
        self.__ativo = False
        print("Usuario desativado com exito.")

        