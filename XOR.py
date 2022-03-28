def huit_bits(nb):
    """
    :param nb: STR -> Un nombre en bianire sous la forme d'une chaîne de caractères
    :return: STR -> Le même nombre écris sur 8 bits
    """

    while len(nb) < 8:
        nb = "0" + nb

    return nb


def xor_encrypt(msg, key):
    """
    :param msg: STR -> Une chaîne de caractère
    :param key: STR -> Un nombre en binaire sous la forme d'une chaîne de caractères
    :return: STR -> Le message codé par la méthode xor
    """

    c_msg = ""
    key = huit_bits(key)

    for c in msg:
        c = huit_bits(bin(ord(c))[2:])
        c_c = ""
        for i in range(len(c)):
            c_c += str(int(c[i]) ^ int(key[i]))
        c_msg += chr(int(c_c, 2))

    return c_msg
