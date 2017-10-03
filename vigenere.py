plaintext=input()
keyword=input()
def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    while len(plaintext) > len(keyword):
        keyword += keyword
    while len(keyword) > len(plaintext):
        keyword = keyword[:-1]
    for i in range(0,len(plaintext)):
        if (ord(plaintext[i]) + ord(keyword[i]) - 65 > 0) and (ord(plaintext[i]) + ord(keyword[i]) - 65 < 27):
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i]) - 65)
        elif not((ord(plaintext[i]) + ord(keyword[i]) - 65 > 0)) or not((ord(plaintext[i]) + ord(keyword[i]) - 65 < 27)):
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i]) - 26 - 65)
        elif (ord(plaintext[i]) + ord(keyword[i]) - 97 > 0) and (ord(plaintext[i]) + ord( keyword[i]) - 97 < 27):
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i])-97)
        else:
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i]) - 26 - 97)
    return print(ciphertext)

encrypt_vigenere(plaintext,keyword)