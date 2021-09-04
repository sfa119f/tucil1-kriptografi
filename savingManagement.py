import json

dictionary = {
  'data': []
}

def downloadJson():
# Download JSON file yang berisi value yang disimpan
  json_object = json.dumps(dictionary, indent=2)
  with open("result.json", "w") as outfile:
    outfile.write(json_object)

def addToJson(isEncrypt, encryptType, key, outputValue, isFile):
# Menambah value ke dictionary yang akan di download nantinya (simpan value)
  temp = {
    'isEncrypt': isEncrypt,
    'isFile': isFile,
    'encryptType': encryptType,
    'value': outputValue
  }
  if (encryptType == 'Affine Cipher'):
    temp['mKey'] = key['mKey']
    temp['bKey'] = key['bKey']
  else:
    temp['key'] = key
  dictionary['data'].append(temp)