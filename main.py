# Caixa eletronico de criptomoedas
import user
import gerenciador_user

manager = gerenciador_user

print("Bem-vindo ao caixa eletronico MONEYGUARD")
print("Selecione uma opção")
print("""
A - Registre sua conta de cripto
B - Acesse sua conta de cripto
C - Fazer uma Transação
D - Cobrar valores
E - Pagar uma conta
""")
option = input(str("> "))

def register(user: str, password: str):
    
def get_option(option: str):
    match option:
        case "A":
            print("Crie sua primeira conta de criptomoedas na MoneyGuard")
            nome = input(str("Digite seu nome completo: "))
            cpf = input(str("Digite o numero do seu CPF: "))
            password = input("Digite a senha da sua conta: ")
            try:
                manager.register()
            except Exception as e:
                print(e)
        case "B":
            print("Bem-vindo a Tela de Login")
            cpf = input(str("Digite seu CPF: "))
            password = input("Digite a senha da sua conta: ")
            try:
                manager.login()
            except Exception as e:
                print(e)
