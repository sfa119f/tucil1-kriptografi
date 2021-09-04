def readMatriks (namaFile):
# Membaca file matriks full vigenere
    f = open ( namaFile , 'r')
    matriks = []
    matriks = [ line.split() for line in f]
    return matriks

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

def makeKey(plainText,key):
# Mengubah key sesuai dengan format huruf besar dan mengulang char pada key sehingga panjang key = plaintext
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
            k = key[i%len(key)] 
            key.append(k)
            newKey = "".join(key) # Menggabungkan huruf menjadi kata
        return newKey
    else:
        return key

def fullCipher(plainText,key,matriks):
# Melakukan enkripsi plainText menjadi cipherText
# Formula : Matriks vigenere merupakan urutan alfabet acak yang merupakan permutasi dari huruf alfabet
    p = makePlain(plainText)
    k = makeKey(p,key)
    pN = []
    kN = []
    res = []
    for i in range (len(p)):
        n = ord(p[i]) - ord('A') # Mengubah huruf menjadi angka
        pN.append(n)
        m = ord(k[i]) - ord('A') # Mengubah huruf menjadi angka
        kN.append(m)
        r = matriks[kN[i]][pN[i]] # Mencari nilai pada matriks untuk key[i] dan plainText[i]
        res.append(chr(int(r)+ord('A'))) # Mengubah angka menjadi huruf
        cip = "".join(res) # Menggabungkan huruf
    return cip

def fullPlain(cipherText, key, matriks):
# Melakukan enkripsi plainText menjadi cipherText
# Formula : Matriks vigenere merupakan urutan alfabet acak yang merupakan permutasi dari huruf alfabet
    k = makeKey(cipherText,key)
    cN = []
    kN = []
    res = []
    for i in range (len(cipherText)):
        n = ord(cipherText[i]) - ord('A') # Mengubah huruf menjadi angka
        cN.append(n)
        m = ord(k[i]) - ord('A') # Mengubah huruf menjadi angka
        kN.append(m)
        r = matriks[kN[i]].index(str(cN[i])) # Mencari index pada kolom key[i] yang nilainya = cipherText[i] 
        res.append(chr(int(r)+ord('A'))) # Mengubah angka menjadi huruf
        pl = "".join(res) # Menggabungkan huruf
    return pl