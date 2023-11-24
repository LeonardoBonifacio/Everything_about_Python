from os import system
system('cls')

from random import sample

def embaralharString(string):
    embaralhada = sample(string,len(string))
    a = ''.join(embaralhada)
    print(a)

embaralharString('Python')