def makePlain(PlainText):
# Mengubah plaintext sesuai dengan format huruf kapital dan membuang angka, spasi, dan tanda baca
    p = []
    plainText = PlainText.upper()
    plain = list(plainText) # Memecah kata menjadi huruf-huruf
    for char in plain:
        if (char.isalpha()):
            p.append(char)
        newP = "".join(p) # Menggabungkan huruf menjadi kata
    return newP

def makeKeyAuto(plainText, key):
# Mengubah key sesuai dengan format huruf besar dan menambah plainText ke belakang key 
# hingga panjang key = plainText
    key = key.upper()
    key = list(key) # Memecah kata menjadi huruf-huruf
    if (len(plainText) < len(key)):
        for i in range (len(plainText)):
            k = key[i]
            key.append(k)
            newKey = "".join(key)
        return newKey 
    elif (len(plainText) > len(key)):
        for i in range (len(plainText)-len(key)):
            k = plainText[i%len(plainText)] # Membuat perulangan key sepanjang plainText
            key.append(k)
            newKey = "".join(key) # Menggabungkan huruf menjadi kata
        return newKey
    else:
        return key

def autoCipher(plainText, key):
# Melakukan enkripsi plainText menjadi cipherText
# Formula : c[j] = E(p[j])  = (p[j] + k[i]) mod 26
    p = makePlain(plainText)
    k = makeKeyAuto(p,key)
    cipher = []
    for i in range (len(p)):
        n = ((ord(p[i]) + ord(k[i])) % 26) + ord('A') # konversi ke angka
        cipher.append(chr(n)) # konversi ke alfabet
        cip = "".join(cipher) # Menggabungkan huruf menjadi kata
    return cip

def autoPlain(cipherText, key):
# Melakukan deskripsi cipherText menjadi plainText
# Formula : p[j] = D(c[j])  = (c[j] - k[i]) mod 26
    if len(key) > len(cipherText):
        key = key[:len(cipherText)]
    plain = []
    for i in range(len(key)): # decrypt sepanjang key
        n = ((ord(cipherText[i]) - ord(key[i]) + 26) % 26) + ord ('A') # konversi ke angka
        plain.append(chr(n)) # konversi ke alfabet
        pl = "".join(plain) # Menggabungkan huruf menjadi kata
    j = 0
    for i in range(len(key), len(cipherText)): # decrypt dari hasil output sementara
        n = ((ord(cipherText[i]) - ord(pl[j]) + 26) % 26) + ord ('A') # konversi ke angka
        plain.append(chr(n)) # konversi ke alfabet
        pl = "".join(plain) # Menggabungkan huruf menjadi kata
        j += 1
    return pl