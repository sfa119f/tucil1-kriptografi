import json

dictionary = {
  'data': []
}

def downloadJson():
  json_object = json.dumps(dictionary, indent=2)
  with open("result.json", "w") as outfile:
    outfile.write(json_object)

def addToJson(isEncrypt, encryptType, key, outputValue):
  temp = {
    'isEncrypt': isEncrypt,
    'encryptType': encryptType,
    'value': outputValue
  }
  if (encryptType == 'Affine Cipher'):
    temp['mKey'] = key['mKey']
    temp['bKey'] = key['bKey']
  else:
    temp['key'] = key
  dictionary['data'].append(temp)