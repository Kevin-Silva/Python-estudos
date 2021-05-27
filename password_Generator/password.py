import random
import string

print("Olá, iremos gerar uma senha para você.")

tamanho = int(input("Digite o tamanho desejado da senha: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

soma = lower + upper + num + symbols

temporario = random.sample(soma, tamanho)

senha = "".join(temporario)

print(senha)

