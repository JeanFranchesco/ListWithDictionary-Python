import json

def Alterar(choice):
  x=int(input("Alterar\n1 - Nome\n2 - Idade\n3 - Endereco\n4 - Cell\n"))
  match(x):
    case 1:
      registros_carregados[choice-1]["Nome"] = input("Digite seu nome: ")
    case 2:
        registros_carregados[choice-1]["Idade"] = input("Digite sua idade: ")
    case 3:
      registros_carregados[choice-1]["Endereço"] = input("Digite seu endereço: ")
    case 4:
      registros_carregados[choice-1]["Cell"] = input("Digite seu número de celular: ")
  with open(caminho_arquivo, 'w') as arquivo:
    json.dump(registros_carregados, arquivo)
    print(f"Nome do Aluno: {registros_carregados[choice-1]['Nome']}")
    print(f"CPF do Aluno: {registros_carregados[choice-1]['CPF']}")
    print(f"Idade do Aluno: {registros_carregados[choice-1]['Idade']}")
    print(f"Endereço do Aluno: {registros_carregados[choice-1]['Endereço']}")
    print(f"Cell do Aluno: {registros_carregados[choice-1]['Cell']}")

registro=[
    { "Nome":"",
      "CPF":'',
      "Idade":'',
      "Endereço":"",
      "Cell":''
    },
    { "Nome":"",
      "CPF":'',
      "Idade":'',
      "Endereço":"",
      "Cell":''
    },
    { "Nome":"",
      "CPF":'',
      "Idade":'',
      "Endereço":"",
      "Cell":''
    },
    { "Nome":"",
      "CPF":'',
      "Idade":'',
      "Endereço":"",
      "Cell":''
    },
    { "Nome":"",
      "CPF":'',
      "Idade":'',
      "Endereço":"",
      "Cell":''}
]

registros = []
for x in range(5):
    registro[x]["Nome"] = input("Digite seu nome: ")
    registro[x]["CPF"] = input("Digite seu CPF: ")
    registro[x]["Idade"] = input("Digite sua idade: ")
    registro[x]["Endereço"] = input("Digite seu endereço: ")
    registro[x]["Cell"] = input("Digite seu número de celular: ")

caminho_arquivo = 'registros.txt'
with open(caminho_arquivo, 'w') as arquivo:
    json.dump(registro, arquivo)

with open(caminho_arquivo, 'r') as arquivo:
    registros_carregados = json.load(arquivo)

for i, registro in enumerate(registros_carregados):
    print(f"\nRegistro {i + 1}:")
    print(f"Nome do Aluno: {registro['Nome']}")
    print(f"CPF do Aluno: {registro['CPF']}")
    print(f"Idade do Aluno: {registro['Idade']}")
    print(f"Endereço do Aluno: {registro['Endereço']}")
    print(f"Cell do Aluno: {registro['Cell']}")
choice= int(input("Digite o número do registro que deseja alterar: "))
Alterar(choice)
