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



print ("""Opérations possibles :
    1- Addition
    2- Soustraction
    3- Multiplication
    4- Division
    5- Puissance d'un nombre
    6- Racine carré
    7- Quotient de division
    8- Reste de division""")


while True: 
    choix = input("Entrez votre choix (1, 2, 3, 4, 5, 6, 7, 8) :")

    if choix in ('1','2','3','4','5','7','8'):
        num1 = float(input("Entrez le premier nombre :"))
        num2 = float(input("Entrez le deuxième nombre :"))

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

    if choix in ('6'):
        num3 = float(input("Entrer le nombre :"))
        if choix == '6' :
            print("racine de", num3, "=", racine(num3))