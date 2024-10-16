# Calculatrice codé en Python by ACHART Axel

from math import *


def addition(x,y):
    return x + y

def soustraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y 

def puissance (x,y):
    return x**y

def racine(x):
    return sqrt(x)

def quotient(x,y):
    return x//y

def reste(x,y):
    return x%y

def expo(x):
    return exp(x)

def loga(x):
    return log(x)

# 11
def sinus(x):
    return sin(x)

def cosinus(x):
    return cos(x)

def tangente(x):
    return tan(x)


print ("""Opérations possibles :
    1- Addition
    2- Soustraction
    3- Multiplication
    4- Division
    5- Puissance d'un nombre
    6- Racine carré
    7- Quotient de division
    8- Reste de division
    9- Exponentielle d'un nombre
    10- Logarithme d'un nombre
    11- Trigonométrie [a : sinus, b : cosinus, c : tangente]""")


while True: 
    choix = input("Entrez votre choix (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) :")

    if choix in ('1','2','3','4','5','7','8'):
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))

        if choix == '1' :
            print(num1, "+", num2, "=", addition(num1, num2))

        if choix == '2' :
            print(num1, "-", num2, "=", soustraction(num1, num2))

        if choix == '3' :
            print(num1, "*", num2, "=", multiplication(num1, num2))

        if choix == '4' :
            print(num1, "/", num2, "=", division(num1, num2))

        if choix == '5' :
            print(num1, "**", num2, "=", puissance(num1, num2))

        if choix == '7' :
            print(num1, "//", num2, "=", quotient(num1, num2))

        if choix == '8' :
            print(num1, "%", num2, "=", reste(num1, num2))

    if choix in ('6','9','10'):
        num3 = float(input("Entrez le nombre : "))
        if choix == '6' :
            print("racine de", num3, "=", racine(num3))
    
        if choix == '9' :
            print("exponentielle de", num3, "=", expo(num3))
    
        if choix == '10' :
            print("logarithme de", num3, "=", loga(num3))
    
    if choix in ('11'):
        choix = input("Entrez votre choix de fonction (a, b, c) :")

        if choix == 'a':
            num4 = float(input("Entrez le nombre : "))
            print("sinus de", num4, "=", sinus(num4), "rad")

        if choix == 'b':
            num5 = float(input("Entrez le nombre : "))
            print("cosinus de", num5, "=", cosinus(num5), "rad")
        
        if choix =='c':
            num6 = float(input("Entrez le nombre : "))
            print("tangente de", num6, "=", tangente(num6), "rad")
