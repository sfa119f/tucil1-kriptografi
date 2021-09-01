def invMod(val1, val2):
  a, b, x, y, u, v =  val1, val2, 0, 1, 1, 0
  while a != 0:
    q = b // a
    r = b % a
    m = x - u * q
    n = y - v * q
    b, a, x, y, u, v = a, r, u, v, m, n
  if b != 1:
    return None
  return x % val2

def encryptAfnC(mKey, bKey, text):
  res = ''
  for i in range(len(text)):
    res += chr((mKey * (ord(text[i]) - ord('A')) + bKey) % 26 + ord('A'))
  return res

def decryptAfnC(mKey, bKey, cipher):
  iMod = invMod(mKey, 26)
  if iMod == None:
    return None
  res = ''
  for i in range(len(cipher)):
    res += chr((iMod * (ord(cipher[i]) - ord('A') - bKey)) % 26 + ord('A'))
  return res