def creer_grille():
    """IN : None
    OUT : LIST x 2
    Crée la grille de Vigenère"""

    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    grille = []

    for x in range(len(a)):
        grille.append([])
        for y in range(len(a)):
            i = (x + y) % len(a)
            grille[x].append(a[i])

    return a, grille


def recherche(t, e):
    """IN : LIST, e
    OUT : INT
    Donne l'indice de l'élément e s'il se trouve dans le tableau"""

    for i in range(len(t)):
        if e == t[i]:
            return i
    return None


def vigenere(msg, key):
    """IN : STR, STR
    OUT : STR
    Code le message grâce à la clé et à la méthode de vigenere"""

    a, grille = creer_grille()  # Initialisations
    key = key.upper()           #
    msg = msg.upper()           #
    c_msg = ''                  #

    ki = 0
    for i in range(len(msg)):
       
        ki = ki % len(key)           # Si le message est plus grand que la clé, cette dernière boucle
       
        rki = recherche(a, key[ki])  # On recherche la ligne de la letre de la clé
        rmi = recherche(a, msg[i])   # On recherche la colonne de la letre du message

        c_msg += grille[rki][rmi]    # On ajoute la lettre trouvée grâce aux indices précédents

        ki += 1
       
    return c_msg


def devigenere(c_msg, key):
    """IN : STR, STR
    OUT : STR
    Décode le message grâce à la clé et à la méthode de vigenere"""
   
    a, grille = creer_grille()    # Initialisations
    key = key.upper()             #
    c_msg = c_msg.upper()         #
    msg = ''                      #

    ki = 0
    for i in range(len(c_msg)):
       
        ki = ki % len(key)                     # Si le message est plus grand que la clé, cette dernière boucle

        rki = recherche(a, key[ki])            # On recherche la ligne de la letre de la clé
        rmi = recherche(grille[rki], c_msg[i]) # On recherche l'indice de la lettre décodée

        msg += a[rmi]                          # On ajoute la lettre décodée au message
       
        ki += 1
   
    return msg
