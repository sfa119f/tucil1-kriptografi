def encryptEVC(key, text):
  j, res = 0, ''
  for i in range(len(text)):
    j %= len(key)
    res += chr((ord(text[i]) + ord(key[j])) % 256)
    j += 1
  return res

def decryptEVC(key, cipher):
  j, res = 0, ''
  for i in range(len(cipher)):
    j %= len(key)
    res += chr((ord(cipher[i]) - ord(key[j])) % 256)
    j += 1
  return res