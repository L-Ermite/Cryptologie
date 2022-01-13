def creer_grille():

    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    grille = []

    for x in range(len(a)):
        grille.append([])
        for y in range(len(a)):
            if y+x >= len(a):
                i = y + x - len(a)
            else:
                i = x + y
            grille[x].append(a[i])

    return a, grille


def recherche(t, e):

    for i in range(len(t)):
        if e == t[i]:
            return i
    return None


def vigenere(msg, key):

    a, grille = creer_grille()
    key = key.upper()
    msg = msg.upper()
    c_msg = ''

    for i in range(len(msg)):
        if i >= len(key):
            ki = i - len(key)
        else:
            ki = i

        rki = recherche(a, key[ki])
        rmi = recherche(a, msg[i])

        c_msg += grille[rki][rmi]

    return c_msg


def devigenere(c_msg, key):

    a, grille = creer_grille()
    key = key.upper()
    c_msg = c_msg.upper()
    msg = ''

    for i in range(len(c_msg)):
        if i >= len(key):
            ki = i - len(key)
        else:
            ki = i

        rki = recherche(a, key[ki])
        rmi = recherche(grille[rki], c_msg[i])

        msg += a[rmi]

    return msg
