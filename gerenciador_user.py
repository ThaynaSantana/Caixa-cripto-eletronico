import user

# array de usuarios cadastrados
users = ()

def register(self, nome, cpf, password):
    self.nome = nome
    self.cpf = cpf
    self.password
    try:
        user = User(nome,cpf,password)
        users.append(user)
        print("Usuario registrado com sucesso!")
    except Exception as e:
        print(e)
        print("não foi possivel fazer o registro")
