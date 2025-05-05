#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d’un entier n de façon récursive.

    Paramètres:
    n (int): Un entier non négatif pour lequel on souhaite calculer la factorielle.

    Retour:
    int: La factorielle de n (n!), c’est-à-dire le produit de tous les entiers de 1 à n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Récupère l'argument en ligne de commande, le convertit en entier et calcule sa factorielle
f = factorial(int(sys.argv[1]))
print(f)

