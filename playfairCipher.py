def makeKey(key):
# Membuat key sesuai dengan aturan playfair cipher
# Membuang huruf 'j' jika ada di key dan menambahkan semua huruf alfabet yang belum ada pada key 
  res = "".join(dict.fromkeys(key)).replace('J', '')
  for i in range(65,91):
    if i != 74 and (chr(i) not in res):
      res += chr(i)
  return res

def encryptPfC(key, text):
# Melakukan enkripsi plain text menjadi cipher text
# Mengganti huruf 'J' dengan 'I' pada plain text
# Bagi plain text menjadi pasangan 2 huruf
# Jika ada huruf yang sama, maka sisipkan 'X' yang ditengah contohnya spasi
# Jika jumlah huruf ganjil, maka sisipkan 'X' di bagian akhir
# Formula : Jika dua huruf terdapat pada baris kunci yang sama maka tiap huruf 
# diganti dengan huruf di kanannya
# Jika dua huruf terdapat pada kolom kunci yang sama maka tiap huruf
# diganti dengan huruf di bawahnya
# Jika dua huruf tidak pada baris yang sama atau kolom yang sama maka diganti huruf pada perpotongan 
# baris dan kolom antara huruf pertama dan huruf kedua
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
# Melakukan dekripsi cipher text menjadi plain text
# Jika dua huruf terdapat pada baris bujursangkar yang sama maka
# tiap huruf diganti dengan huruf di kirinya
# Jika dua huruf terdapat pada kolom bujursangkar yang sama maka
# tiap huruf diganti dengan huruf di atasnya
# Jika dua huruf tidak pada baris yang sama atau kolom yang sama ,
# maka huruf pertama diganti dengan huruf pada perpotongan baris
# huruf pertama dengan kolom huruf kedua . Huruf kedua diganti
# dengan huruf pada titik sudut keempat dari persegi panjang yang
# dibentuk dari tiga huruf yang digunakan sampai sejauh ini
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