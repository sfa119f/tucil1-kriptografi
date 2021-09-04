def encryptEVC(key, text):
# Melakukan enkripsi plain text menjadi cipher text (Extended Vigenere Cipher)
# Karakter yang digunakan sebanyak 256 karakter (ASCII)
  j, res = 0, ''
  for i in range(len(text)):
    j %= len(key)
    res += chr((ord(text[i]) + ord(key[j])) % 256)
    j += 1
  return res

def decryptEVC(key, cipher):
# Melakukan deskripsi cipher text menjadi plain text (Extended Vigenere Cipher)
# Karakter yang digunakan sebanyak 256 karakter (ASCII)
  j, res = 0, ''
  for i in range(len(cipher)):
    j %= len(key)
    res += chr((ord(cipher[i]) - ord(key[j])) % 256)
    j += 1
  return res