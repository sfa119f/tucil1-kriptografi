import random

def makePlain(PlainText):
    p = []
    plainText = PlainText.upper()
    plain = list(plainText)
    for char in plain:
        if (char.isalpha()):
            p.append(char)
        newP = "".join(p)
    return newP

def makeKey(plainText,key):
    key = key.upper()
    key = list(key) # Memecah kata menjadi huruf-huruf dalam array
    if (len(plainText) == len(key)): 
        return key
    else:
        for i in range (len(plainText)-len(key)):
            k = key[i%len(key)] # Membuat perulangan key sepanjang plainText
            key.append(k)
            newKey = "".join(key)
        return newKey

def makeKeyAuto(plainText, key):
    key = key.upper()
    key = list(key)
    if (len(plainText) == len(key)):
        return key
    else:
        for i in range (len(plainText)-len(key)):
            k = plainText[i%len(plainText)] # Membuat perulangan key sepanjang plainText
            key.append(k)
            newKey = "".join(key)
        return newKey

def cipherVigenere(plainText, key):
    cipher = []
    for i in range (len(plainText)):
        n = (ord(plainText[i]) + ord(key[i])) % 26
        n += ord('A')
        cipher.append(chr(n))
        cip = "".join(cipher)
    return cip

def plainVigenere(cipherText, key):
    plain = []
    for i in range(len(cipherText)):
        n = (ord(cipherText[i]) - ord(key[i]) + 26) % 26
        n += ord ('A')
        plain.append(chr(n))
        pl = "".join(plain)
    return pl

a = "negara penghasil minyak"
b = "INDO"

c = makePlain(a)
k = makeKeyAuto(c,b)
print(c)
print(k)
h = cipherVigenere(c,k)
print("Cipher Text: " + h)
p = plainVigenere(h,k)
print("Plain Text: " + p)
        
