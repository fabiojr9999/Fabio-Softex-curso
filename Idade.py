from ast import While
import datetime
from datetime import date

nome = input ('Digite o nome:')
dia =int(input('Digite o dia do nascimento:'))
while (dia == 0 or dia >= 42):
  print ('dia inexistente, digite um numero entre 1 e 41.')
  dia =int(input('digite o dia do nascimento:'))

mes = int(input('digite o mes do nascimento:'))
while (mes ==0 or mes >=13):
    print('digite o mes do seu aniversario, entre 1 e 12')
    mes=int(input('digite qual o mes do nascimento:'))

ano = int(input('digite o ano do nascimento:'))
while (ano <=1921 or ano >=2022):
    print('ano invalido, insira uma data entre os anos 1922 e 2023') 
    ano = int(input('Digite o ano de Nascimento:'))

nascimento =datetime.date(ano, mes, dia)

idade = (date.today() - nascimento) 
resultado = (idade.days / 365.25)
print('%s tem %d anos' %(nome, resultado))

