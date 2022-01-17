import math
import random


def prime(sup=3):
    """IN : INT (facultatif)
    OUT : INT
    Donne le nombre premier supérieur ou égal à sup"""
    iprime = False

    while not iprime:
        iprime = True

        for x in range(2, int(math.sqrt(sup)+1)):   # On cherhce si sup est divisible par un nombre entier inférieur ou égal à sa racine carrée
            if sup % x == 0:
                iprime = False
                break

        if iprime:
            return sup

        sup += 1


def bezout(a, b):
    """IN : INT x 2
    OUT : INT x 3
    Calcule les coefficients de Bezou et le PGCD de a,b
    Algorithme trouvé sur :
    https://www.rookieslab.com/posts/extended-euclid-algorithm-to-find-gcd-bezouts-coefficients-python-cpp-code"""
    s, os = 0, 1
    t, ot = 1, 0
    r, oldr = b, a

    while r != 0:
        q = oldr // r
        oldr, r = r, oldr % r
        os, s = s, os - q * s
        ot, t = t, ot - q * s

    return oldr, os, ot


def rsa(sup=0):
    """IN : Int (facultatif)
    OUT : Int
    donne la clé publique, la clé privée et l'indicatrice d'Euler
    si sup est != 0, les nb premiers p et q seront supérieurs ou égaux à sup"""

    p = prime(sup + random.randint(0, 1000))    # On choisi des valeurs aléatoires
    q = prime(p + random.randint(1, 1000))

    n = p * q
    ieuler = (p - 1) * (q - 1)

    e = 2
    primewith = 0
    while not primewith:
        if bezout(e, ieuler)[0] == 1:    # On verifie qu'il sont premiers entre eux grace au PGCD
            primewith = True
            e -= 1                      # On annule le += qui suit
        e += 1

    d = bezout(e, ieuler)[1]             # https://fr.wikipedia.org/wiki/Inverse_modulaire

    c_pu = (e, n)
    c_pr = (d, n)

    return c_pu, c_pr


def encrypt(e, n, msg):
    """IN : INT x 3
    OUT : INT
    Donne le chiffre encrypté par la méthode RSA"""
    return (msg ** e) % n


def decrypt(d, n, c_msg):
    """IN : INT x 3
        OUT : INT
        Donne le chiffre décrypté par la méthode RSA"""
    return (c_msg ** d) % n
