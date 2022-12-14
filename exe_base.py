#!/usr/bin/env python
# coding: utf-8

# Programa que pede a temperatura em graus Fahrenheit, transforma e mostra a temperatura em graus Celsius. 

# In[ ]:


fahrenheit = int(input('quantos Fahrenheit está fazendo ai?: '))

fahrenheit -= 32
fahrenheit /= 9
fahrenheit *= 5
celsius = fahrenheit
print('então está fazendo', celsius, 'por ai!')


# Programa que pede a temperatura em graus Celsius, transforma e mostra a temperatura em graus Fahrenheit. 

# In[34]:


celsius = int(input('quantos celsius está fazendo ai?: '))

celsius *= 1.8
celsius += 32
fahrenheit = celsius

print(f'então está fazendo {fahrenheit:.2f}, por ai!')
    


# Programa que identifica se há vogal ou consoante 

# In[69]:


alfa = input("Informe uma letra ou consoante:")

if alfa.isalpha():
    if alfa =="a":
        print("Vogal")
    elif alfa == "e":
        print("Vogal")
    elif alfa == "i":
        print("Vogal")
    elif alfa == "o":
        print("Vogal")
    elif alfa == "u":
        print("Vogal")
        print("Insira uma letra ou consoante")
    else:
        print("Consoante")
else:
    print("Não é uma letra!")


# Programa que lê três números e mostre o maior e menor deles. 

# In[81]:


a = int(input('insira um número natural: '))
b = int(input('insira um número natural: '))
c = int(input('insira um número natural: '))

valmax = max(a, b, c)
print(f'o valor maximo entre eles é {valmax}')

valmini = min(a, b, c)
print(f'o valor mínimo entre eles é {valmini}')


# Programa que lê três números e mostre o maior e o menor deles. 

# In[ ]:


a = int(input('insira um número natural: '))
b = int(input('insira um número natural: '))
c = int(input('insira um número natural: '))

maxi = a    
if b > maxi:
    maxi = b
    
if c >maxi:
    maxi = c

print(f'esse é o maior número {maxi}')

mini = a

if b < mini:
    mini = b
    
if c < mini:
    mini = c
    
print(f'esse é o menor número {mini}')


# Programa que lê três números e mostra-os em ordem crescente decrescente. 

# In[6]:


lista = []
for i in range(3):
    elemento = int(input('Digite um numero: '))
    lista.append(elemento)

lista.sort(reverse = True)
print(lista)

lista.sort()
print(lista)


# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%  
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%  
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%  
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:  
#     o salário antes do reajuste;  
#     o percentual de aumento aplicado;  
#     o valor do aumento;  
#     o novo salário, após o aumento.   

# In[ ]:


salary = float(input('coloque seu salário: '))
    
if salary <= 280:
    readjustment = salary * 0.2
    salaryincreased = salary + readjustment
    print('mensagem')
    print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
    print(f'valor do aumento:{readjustment}, sob um persentual de 20%')


if salary > 280 and salary <= 700:
    readjustment = salary * 0.15
    salaryincreased = salary + readjustment
    print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
    print(f'valor do aumento:{readjustment}, sob um persentual de 15%')


if salary > 700 and salary <= 1500:
    readjustment = salary * 0.1
    salaryincreased = salary + readjustment
    print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
    print(f'valor do aumento:{readjustment}, sob um persentual de 10%')

if salary > 1500:
    readjustment = salary * 0.05
    salaryincreased = salary + readjustment
    print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
    print(f'valor do aumento:{readjustment}, sob um persentual de 5%')


# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
# 

# In[ ]:


val = int(input('escreve um número ai, ninguém se importa Brasil perdeu a copa: '))

if val < 0 or val > 10:
    print('esse é um número inválido, digite novamente')
    
else:
    print('legal')
    


# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# 
#    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:  
#     salários até R$ 280,00 (incluindo) : aumento de 20%  
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%  
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%  
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:  
#     o salário antes do reajuste;  
#     o percentual de aumento aplicado;  
#     o valor do aumento;  
#     o novo salário, após o aumento.   

# In[ ]:


salary = input('coloque seu salário: ')

if type(salary) == int:

    if salary >= 280:
        readjustment = salary * 0.2
        salaryincreased = salary + readjustment
        print('mensagem')
        print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
        print(f'valor do almento:{readjustment}, sob um persentual de 20%')


    if salary <= 700:
        readjustment = salary * 0.15
        salaryincreased = salary + readjustment
        print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
        print(f'valor do almento:{readjustment}, sob um persentual de 15%')


    if salary <= 1500:
        readjustment = salary * 0.1
        salaryincreased = salary + readjustment
        print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
        print(f'valor do almento:{readjustment}, sob um persentual de 10%')

    if salary > 1500:
        readjustment = salary * 0.05
        salaryincreased = salary + readjustment
        print(f'seu salário de {salary}, passa a ser agora de {salaryincreased}, parabéns!')
        print(f'valor do almento:{readjustment}, sob um persentual de 5%')

else:
    print('digite apenas valores numéricos, por favor!')


# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

# In[93]:


nome = input('digite um nome: ')
senha = input('digite uma senha: ')

while senha == nome:
    print('opa, nome e senha não podem ser iguais!')
    senha = input('digite uma nova senha: ')


# -Faça um programa que leia e valide as seguintes informações:
# 
#    1.Nome: maior que 3 caracteres  
#    2.Idade: entre 0 e 150;  
#    3.Salário: maior que zero;  
#    4.Sexo: 'f' ou 'm';  
#    5.Estado Civil: 's', 'c', 'v', 'd'; 

# In[15]:



while True:
    
    name = input('insira seu nome: ')
    if ( len(name) <=  3 ):
        print('opa, seu nome deve ter mais de 3 caractéres')
        name = input('insira seu nome: ')
    
    age = int(input('insira sua idade: '))
    if ( age > 150 or age < 0 ):
        print('sua idade é inválida')
        age = int(input('insira uma idade acima de 0 e abaixo de 150: '))
    
    salary = int(input('insira seu salario: '))
    if salary <= 0:
        print('seu salário não pode ser igual a zero!')
        salary = int(input('insira seu salario: '))

    sexo = input('insira seu sexo biológico: ')
    if sexo.upper() != 'F' and sexo.upper() != 'M':
        print('desculpe mona, apenas sexos biologicos aceitos aqui')
        sexo = input('insira seu gênero normativo: ')
        
    maritalstatus = input('insira seu estado civil: ')
    if maritalstatus.upper() != 'S' and maritalstatus.upper() != 'C' and maritalstatus.upper() != 'V' and maritalstatus.upper() != 'D':
        print('status não válido')
        sexo = input('insira um status válido: ')
    break


# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 
#    "Telefonou para a vítima?"  
#     "Esteve no local do crime?"  
#     "Mora perto da vítima?"  
#     "Devia para a vítima?"  
#     "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

# In[30]:


provas = 0
positiva = 'sim'
negativa = 'não'

#validação para que o campo receba apenas as respostas "sim" e "não"
def satisfy_input(prompt):
    while True:
        try:
            value = (input(prompt))
        except ValueError:
            print('desculpe, não entendi isso')
            continue
        
        if value.lower().replace(" ", "") != positiva and value.lower().replace(" ", "") != negativa:
            print('responda apenas com "sim" ou "não, por favor"')
            continue
        else:
            break
            
    return value

#armazena as respostas positivas na variável provas
resposta1 = satisfy_input('Telefonou para a vítima? ')
if resposta1 == positiva:
    provas += 1

resposta2 = satisfy_input('Esteve no local do crime? ')
if resposta2 == positiva:
    provas += 1

resposta3 = satisfy_input('Mora perto da vítima? ')
if resposta3 == positiva:
    provas += 1

resposta4 = satisfy_input('Devia para a vítima? ')
if resposta4 == positiva:
    provas += 1

resposta5 = satisfy_input('Já trabalhou com a vítima? ')
if resposta5 == positiva:
    provas += 1
    
#classifica o nível de envolvimento com o crime apartir das provas

if provas < 2:
    print('você é inoscente')
    
if provas == 2:
    print('você está classificado como suspeito')
    
if provas == 3 or provas == 4:
    print('você foi cumplisse nesse assassinato!')
    
if provas == 5:
    print('você é o assassino!')


# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 
# 

# In[92]:


year = input('insira um número correspondente a um ano: ')

#primeira validação rejeita letras
while year.isalpha():
    print('digite apenas números por favor!')
    year = input('insira um número correspondente a um ano: ')
    
#segunda validação aceita apena campo com 4 digitos
if len(year) == 4:
    year = int(year)
    
    if year % 4 == 0:
        print('esse ano será bissexto!')
    
    elif year % 100 != 0:
        print('esse ano será bissexto!')
        
    else:
        print('esse ano não será bissexto!')
else:
    print('Desculpe, preciso que digite o ano com os 4 digitos')


# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# 
#    Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;  
#     Triângulo Equilátero: três lados iguais;  
#     Triângulo Isósceles: quaisquer dois lados iguais;  
#     Triângulo Escaleno: três lados diferentes;   

# In[ ]:


lado1 = input('digite um lados do triangulo')
lado2 = input('digite outro dos lados do triangulo')
lado3 = input('digite outro dos lados do triangulo')

if lado1 + lado2 < lado3:
    print(1opa, isso não é um triangulo)
    
if lado1 == lado2 and lado2 == lado3:
    print('esse é um triângulo Equilátero')
    
if 


# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

# In[26]:


A = 80000
B = 200000
cresceA = 0
cresceB = 0
anos = 0

while B > A:
    cresceA = A * 0.3
    cresceB = B * 0.15
    
    A += cresceA
    B += cresceB
    anos += 1
    
print(f'foram necessários {anos} anos para as populações se igualarem')


# In[ ]:





# In[11]:


a = []

for i in range(1, 21):
    a.append(i)
print(a)


# In[ ]:




