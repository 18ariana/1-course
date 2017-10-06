def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    high_register = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_register = 'abcdefghijklmnopqrstuvwxyz'
    while len(plaintext) > len(keyword):
        keyword += keyword
    while len(keyword) > len(plaintext):
        keyword = keyword[:-1]
    ciphertext = ''
    shift = [0] * len(keyword)
    for i in range(0, len(keyword)):
        if keyword[i] in small_register:
            shift[i] = small_register.index(keyword[i])
            if (ord(plaintext[i]) + shift[i] > 96) and (ord(plaintext[i]) + shift[i] < 123):
                ciphertext += chr(ord(plaintext[i]) + shift[i])
            else:
                ciphertext += chr(ord(plaintext[i]) + shift[i] - 26)
        elif keyword[i] in high_register:
            shift[i] = high_register.index(keyword[i])
            if (ord(plaintext[i]) + shift[i] > 64) and (ord(plaintext[i]) + shift[i] < 91):
                ciphertext += chr(ord(plaintext[i]) + shift[i])
            else:
                ciphertext += chr(ord(plaintext[i]) + shift[i] - 26)
    return print(ciphertext)


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    high_register = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_register = 'abcdefghijklmnopqrstuvwxyz'
    while len(ciphertext) > len(keyword):
        keyword += keyword
    while len(keyword) > len(ciphertext):
        keyword = keyword[:-1]
    plaintext = ''
    shift = [0] * len(keyword)
    for i in range(0, len(keyword)):
        if keyword[i] in small_register:
            shift[i] = small_register.index(keyword[i])
            if (ord(ciphertext[i]) - shift[i] > 96) and (ord(ciphertext[i]) - shift[i] < 123):
                plaintext += chr(ord(ciphertext[i]) - shift[i])
            else:
                plaintext += chr(ord(ciphertext[i]) - shift[i] + 26)
        elif keyword[i] in high_register:
            shift[i] = high_register.index(keyword[i])
            if (ord(ciphertext[i]) - shift[i] > 64) and (ord(ciphertext[i]) - shift[i] < 91):
                plaintext += chr(ord(ciphertext[i]) - shift[i])
            else:
                plaintext += chr(ord(ciphertext[i]) - shift[i] + 26)
    return plaintext
