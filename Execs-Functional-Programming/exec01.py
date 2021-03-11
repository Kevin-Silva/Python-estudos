"""
* Criar variáveis para nome(str), idade(int),
* altura(float), peso(float) de uma pessoa,
* Criar variável com ano atual(int),
* Obter o ano de nascimento da pessoa(baseado na idade e no ano atual)
* Obter o imc da pessoa com 2 casa decimais(Peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-String
"""
nome = "Kevin"
idade = 25
altura = 1.77
peso = 75.00
anoAtual = 2021

anoCalculo = anoAtual - idade
imc = peso / (altura * 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {anoCalculo}.')
