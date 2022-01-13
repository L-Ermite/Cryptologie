def xor_encrypt(msg, key, char=False, csv=False, debug_mode=False):
    """IN : INT or STR, INT or STR (BINARY) , BOOL x 3 (optional)
    OUT : STR
    Code le msg avec la méthode XOR
    Possède plusieurs paramètres:
        char convertis les résultats binaires en caractères unicodes
        csv  indique que les valeurs sont séparées par des virgules
        debug_mode donne plusieurs information en plus du message codé"""

    debug_data = {'original_type': type(msg), 'key_type': type(key)}  # initialisation de plusieurs variables
    encoded_message = ''
    encoded_message_char = ''

    if type(msg) == int:
        msg = str(msg)

    if csv:                                     # Formation de groupe en fonction :
        msg = msg.split(',')                    # - des virgules qui séparaient les données
    else:                                       #
        msg = [bin(ord(c))[2:] for c in msg]    # - du résultat du ord() de chaque caractère du message

    if type(key) == int:
        key = bin(key)  # On convertit la clé en binaire
    if key[1] == 'b':       # Si la clé est au format 0b...
        key = key[2:]

    debug_data['key'] = int(key, 2)     #
    debug_data['msg'] = msg             # Création de plusieurs catégories pour le debug_mode
    debug_data['coded_no_grp'] = ''     #
    debug_data['grp'] = []              #

    ki = 0                              # Les festivités commencent :
    for c in msg:                       # On boucle sur les groupent
        groupping = ''
        for i in range(len(c)):         # Puis sur les bits individuels

            if ki >= len(key):          # Si jamais le message est plus long que la clé ...
                ki = 0                  # ... on recommence au début de cette dernière

            debug_data['coded_no_grp'] += str(int(key[ki]) ^ int(c[i]))+','     # Pour voir ce qui c'est passé en debug
            groupping += str(int(key[ki]) ^ int(c[i]))                          # On reforme les groupes
            ki += 1

        encoded_message += groupping+','                 # La production finale si char est désactivé
        debug_data['grp'].append(groupping)              # Surtout utile avec char d'activé pour voir les valeur avant chr()

        if char:
            encoded_message_char += chr(int(groupping, 2))      # On convertit en caractère Unicode

    if char:                                                    # Puis on remplace l'ancien message
        encoded_message = encoded_message_char

    if debug_mode:
        return encoded_message, debug_data
    else:
        return encoded_message
