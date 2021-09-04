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
# Mengubah key sesuai dengan format huruf besar dan menambah plainText ke belakang key hingga panjang key = plainText
    key = key.upper()
    key = list(key) # Memecah kata menjadi huruf-huruf
    if (len(plainText) == len(key)):
        return key
    else:
        for i in range (len(plainText)-len(key)):
            k = plainText[i%len(plainText)] # Membuat perulangan key sepanjang plainText
            key.append(k)
            newKey = "".join(key) # Menggabungkan huruf menjadi kata
        return newKey

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
    return cip, p

def autoPlain(cipherText, plainText,key):
# Melakukan deskripsi cipherText menjadi plainText
# Formula : p[j] = D(c[j])  = (c[j] - k[i]) mod 26
    k = makeKeyAuto(plainText,key)
    plain = []
    for i in range(len(cipherText)):
        n = ((ord(cipherText[i]) - ord(k[i]) + 26) % 26) + ord ('A') # konversi ke angka
        plain.append(chr(n)) # konversi ke alfabet
        pl = "".join(plain) # Menggabungkan huruf menjadi kata
    return pl

"""a = "thisplaintext"
b = "SONY"

x,y = autoCipher(a,b)
print(x)
print(y)
z = autoPlain(x,y,b)
print(z)"""