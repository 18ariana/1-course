def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    text = plaintext
    key = keyword.lower()
    ciphertext = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        wcode = ord(text[i])
        kcode = abc.find(key[i % len(key)])
        if (97 <= wcode <= 122):
            if (97 <= wcode + kcode <= 122):
                ciphertext += chr(wcode + kcode)
            else:
                ciphertext += chr(wcode + kcode - 26)

        if (65 <= wcode <= 90):
            if (65 <= wcode + kcode <= 90):
                ciphertext += chr(wcode + kcode)
            else:
                ciphertext += chr(wcode + kcode - 26)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    text = str(ciphertext)
    key = str(keyword).lower()
    plaintext = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        wcode = ord(text[i])
        kcode = abc.find(key[i % len(key)])
        if (97 <= wcode <= 122):
            if (97 <= wcode - kcode <= 122):
                plaintext += chr(wcode - kcode)
            else:
                plaintext += chr(wcode - kcode + 26)

        if (65 <= wcode <= 90):
            if (65 <= wcode - kcode <= 90):
                plaintext += chr(wcode - kcode)
            else:
                plaintext += chr(wcode - kcode + 26)

    return plaintext
