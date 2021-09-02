def makeKey(key):
  res = "".join(dict.fromkeys(key)).replace('J', '')
  for i in range(65,91):
    if i != 74 and (chr(i) not in res):
      res += chr(i)
  return res

def encryptPfC(key, text):
  key = makeKey(key)
  text = text.replace('J', 'I')
  i, result = 0, ''
  while i < len(text):
    c1 = key.find(text[i])
    if (i == len(text) - 1) or (text[i] == text[i+1]):
      text = text[: i+1] + 'X' + text[i+1 :]
      c2 = key.find('X')
    else:
      c2 = key.find(text[i+1])
    if (c1 == c2):
      result += (key[c1] * 2)
    elif (c1 % 5 == c2 % 5):
      result += key[(((c1 // 5 + 1) % 5) * 5) + (c1 % 5)]
      result += key[(((c2 // 5 + 1) % 5) * 5) + (c2 % 5)]
    elif (c1 // 5 == c2 // 5):
      result += key[((c1 // 5) * 5) + ((c1 % 5 + 1) % 5)]
      result += key[((c2 // 5) * 5) + ((c2 % 5 + 1) % 5)]
    else:
      result += key[((c1 // 5) * 5) + (c2 % 5)]
      result += key[((c2 // 5) * 5) + (c1 % 5)]
    i += 2

  return result

def decryptPfC(key, cipher):
  key = makeKey(key)
  i, result = 0, ''
  while i < len(cipher):
    c1 = key.find(cipher[i])
    c2 = key.find(cipher[i+1])
    if (c1 == c2):
      result += (key[c1] * 2)
    elif (c1 % 5 == c2 % 5):
      result += key[(((c1 // 5 - 1) % 5) * 5) + (c1 % 5)]
      result += key[(((c2 // 5 - 1) % 5) * 5) + (c2 % 5)]
    elif (c1 // 5 == c2 // 5):
      result += key[((c1 // 5) * 5) + ((c1 % 5 - 1) % 5)]
      result += key[((c2 // 5) * 5) + ((c2 % 5 - 1) % 5)]
    else:
      result += key[((c1 // 5) * 5) + (c2 % 5)]
      result += key[((c2 // 5) * 5) + (c1 % 5)]
    i += 2

  return result