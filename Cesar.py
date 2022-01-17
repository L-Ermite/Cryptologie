def cesar(msg, n):
    """IN : str, int
    OUT : str"""

    z = ord('z')
    msg = msg.lower()

    c_msg = ''
    for c in msg:

        new_c = ord(c) + n

        if new_c > z:        # On dépasse le 'z'...
            new_c -= 26      # ... donc on retourne au 'a'

        c_msg += chr(new_c)

    return c_msg


def decesar(c_msg, n):
    """IN : str, int
    OUT : str"""
    return cesar(c_msg, 26 - n)
