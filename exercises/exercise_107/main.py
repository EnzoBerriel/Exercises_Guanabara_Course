"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""

#Acessa as Pastas
import sys
import os
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if caminho_raiz not in sys.path:
    sys.path.append(caminho_raiz)

#Código Principal
from exercises import functionCodeBasic
import moeda

functionCodeBasic.título("Exercitando módulos em Python")

num=float(input("Digite um valor: "))
n1=float(input("Digite um valor para adição: "))
n2=float(input("Digite um valor para subtrair: "))
print(f"{num} somado a {n1} é igual a {moeda.aumentar(num,n1)} ")
print(f"O dobro de {num} é igual {moeda.dobro(num)}")
print(f"{num} subtraido a {n2} é igual a {moeda.diminuir(num,n2)} ")
print(f"A metade de {num} é igual a {moeda.metade(num)}")
