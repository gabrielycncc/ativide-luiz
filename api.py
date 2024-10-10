from datetime import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def validar_data(data):
    try:
        return datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return None

def main():
    nome = input("Qual é o seu nome? ").strip()
    if not nome: 
        print("Nome não pode ser vazio.")
        return

    while True:
        data_nascimento_input = input("Digite sua data de nascimento (dd/mm/aaaa): ")
        data_nascimento = validar_data(data_nascimento_input)
        if data_nascimento:
            break
        else:
            print("Data inválida. Por favor, insira no formato dd/mm/aaaa.")

    idade = calcular_idade(data_nascimento)
    print(f"Olá, {nome}! Você tem {idade} anos.")

if __name__ == "__main__":
    main()