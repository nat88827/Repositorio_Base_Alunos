# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',30*'-','|')
print('|',10*'-','CADASTRO',10*'-','|')
print('|',30*'-','|')
nome=input('Nome: ')
idade=int(input('Idade: '))
email=input('Email: ')
senha=(input('Senha: '))
print()
print()
print('|',30*'-','|')
print('| ------USUÁRIO CADASTRADO------ |')
print(f'| Seja bem vindo (a) {nome}')
print(f'| Email: {email}')
print('|',30*'-','|')
