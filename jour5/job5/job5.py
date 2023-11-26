def decale_message(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_decale = ''

    for lettre in message:
        if lettre.isalpha():
            if lettre.isupper():
                index = (alphabet.index(lettre.lower()) + decalage) % 26
                lettre_decalee = alphabet[index].upper()
            else:
                index = (alphabet.index(lettre) + decalage) % 26
                lettre_decalee = alphabet[index]
            message_decale += lettre_decalee
        else:
            message_decale += lettre

    return message_decale

# Exemple d'utilisation :
message_initial = "Jules César a utilisé un décalage de trois lettres"
decalage = 3
message_decale = decale_message(message_initial, decalage)
print("Message initial :", message_initial)
print("Message décalé :", message_decale)
