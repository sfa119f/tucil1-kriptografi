from os import read
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from vigenereCipher import vigenereCipher, vigenerePlain
from fullVigenereCipher import fullCipher, fullPlain, readMatriks
from autoVigenereCipher import autoCipher, autoPlain
from extendedVigenereCipher import encryptEVC, decryptEVC
from playfairCipher import encryptPfC, decryptPfC
from affineCipher import invMod, encryptAfnC, decryptAfnC
from savingManagement import downloadJson, addToJson

def showCipher():
  if cipher.get() == 'Affine Cipher':
    keyLabel.place_forget()
    key.place_forget()
    mKeyLabel.place(x=5, y=75)
    mKey.place(x=90, y=75)
    bKeyLabel.place(x=230, y=75)
    bKey.place(x=320, y=75)
    btnClearKey.place(x=460, y=70)
  else:
    mKeyLabel.place_forget()
    mKey.place_forget()
    bKeyLabel.place_forget()
    bKey.place_forget()
    keyLabel.place(x=5, y=75)
    key.place(x=90, y=75)
    btnClearKey.place(x=460, y=70)
  if cipher.get() == 'Extended Vigenere Cipher':
    outputType.set('No Spaces')
    btnNoSpace.config(state=DISABLED)
    btnN5Letter.config(state=DISABLED)
  else:
    btnNoSpace.config(state=NORMAL)
    btnN5Letter.config(state=NORMAL)

def importFile():
  # clearText()
  # fileName = filedialog.askopenfile().name
  # print(fileName)
  # f = open(fileName, 'rb')
  # content = f.read()
  # print(content)
  # f.close()
  # print(list(map(int,content)))
  # d = open('encryptFile', 'wb')
  # d.write(content)
  # d.close
  # cipher.set('Extended Vigenere Cipher')
  # showCipher()
  # textInput.insert(tkinter.END, content)
  # convertText()
  tkinter.messagebox.showinfo('Error', 'Import file not available')

def swapFunction():
  if encrypt.get() == True:
    btnSwap.config(text='Change to Encrypt')
    labelInput.config(text='Cipher Text')
    labelOutput.config(text='Plain Text')
  else:
    btnSwap.config(text='Change to Decrypt')
    labelInput.config(text='Plain Text')
    labelOutput.config(text='Cipher Text')
  clearText()
  encrypt.set(not encrypt.get())

def clearKey():
  key.delete(0, 'end')
  mKey.delete(0, 'end')
  bKey.delete(0, 'end')

def clearText():
  textInput.delete('1.0', END)
  textOutput.config(state=NORMAL)
  textOutput.delete('1.0', END)
  textOutput.config(state=DISABLED)

def typeOutput():
  textOutput.config(state=NORMAL)
  temp = textOutput.get('1.0', 'end-1c')
  if outputType.get() == 'n-5 Letter':
    res = ' '.join([temp[i:i+5] for i in range(0, len(temp), 5)])
  else:
    res = temp.replace(" ", "")
  textOutput.delete('1.0', END)
  textOutput.insert(tkinter.END, res)
  textOutput.config(state=DISABLED)

def saveToJsonFile():
  convertText()
  if (canSave.get()):
    if cipher.get() == 'Affine Cipher':
      keyValue = {
        'mKey': int(mKey.get()),
        'bKey': int(bKey.get())
      }
    else:
      keyValue = key.get()
    addToJson(encrypt.get(), cipher.get(), keyValue, textOutput.get('1.0', 'end-1c'))
    tkinter.messagebox.showinfo('Success', 'JSON file saved successfully')
  else:
    tkinter.messagebox.showinfo('Error', 'JSON file failed to save')

def downloadJsonFile():
  downloadJson()
  tkinter.messagebox.showinfo('Success', 'JSON file downloaded successfully')

def showOutput(outputValue):
  if cipher.get() != 'Extended Vigenere Cipher':
    if outputType.get() == 'n-5 Letter':
      outputValue = ' '.join([outputValue[i:i+5] for i in range(0, len(outputValue), 5)])

  textOutput.config(state=NORMAL)
  textOutput.delete('1.0', END)
  textOutput.insert(tkinter.END, outputValue)
  textOutput.config(state=DISABLED)
  canSave.set(True)

def convertText():
  canSave.set(False)
  if cipher.get() == 'X':
    tkinter.messagebox.showinfo('Error', 'Cipher type not selected')
  elif textInput.get('1.0', 'end-1c') == '':
    tkinter.messagebox.showinfo('Error', 'No input available')
  elif cipher.get() != 'Affine Cipher' and key.get() == '':
    tkinter.messagebox.showinfo('Error', 'No key available')
  elif cipher.get() == 'Affine Cipher' and (mKey.get() == '' or bKey.get() == ''):
    tkinter.messagebox.showinfo('Error', 'No M-key or B-key available')
  elif cipher.get() == 'Affine Cipher':
    try: 
      int(mKey.get())
      int(bKey.get())
    except ValueError:
      tkinter.messagebox.showinfo('Error', 'M-key or B-key only accept integer value')
    else:
      if int(mKey.get()) > 25 or int(mKey.get()) < 1:
        tkinter.messagebox.showinfo('Error', 'M-key must be in range 1-25')
      elif invMod(int(mKey.get()), 26) == None:
        tkinter.messagebox.showinfo('Error', 'M-key must be a relatively prime with 26')
      else:
        if encrypt.get():
          inputValue = ''.join(filter(str.isalpha, textInput.get('1.0', 'end-1c'))).upper()
          outputValue = encryptAfnC(int(mKey.get()), int(bKey.get()), inputValue)
        else:
          outputValue = decryptAfnC(int(mKey.get()), int(bKey.get()), inputValue)
        showOutput(outputValue)
  else:
    if (cipher.get != 'Extended Vigenere Cipher'):
      inputValue = ''.join(filter(str.isalpha, textInput.get('1.0', 'end-1c'))).upper()
      keyValue = ''.join(filter(str.isalpha, key.get())).upper()
    else:
      inputValue = textInput.get('1.0', 'end-1c')
      keyValue = key.get()

    if cipher.get() == 'Vigenere Cipher Standard':
      if encrypt.get():
        outputValue = vigenereCipher(inputValue, keyValue)
      else:
        outputValue = vigenerePlain(inputValue, keyValue)

    elif cipher.get() == 'Full Vigenere Cipher':
      if encrypt.get():
        outputValue = fullCipher(inputValue, keyValue, readMatriks("matriks.txt"))
      else:
        outputValue = fullPlain(inputValue, keyValue, readMatriks("matriks.txt"))

    elif cipher.get() == 'Auto-key Vigenere Cipher':
      if encrypt.get():
        outputValue = autoCipher(inputValue, keyValue)
      else:
        outputValue = autoPlain(inputValue, keyValue)
        
    elif cipher.get() == 'Extended Vigenere Cipher':
      if encrypt.get():
        outputValue = encryptEVC(keyValue, inputValue)
      else:
        outputValue = decryptEVC(keyValue, inputValue)
    elif cipher.get() == 'Playfair Cipher':
      if encrypt.get():
        outputValue = encryptPfC(keyValue, inputValue)
      else:
        outputValue = decryptPfC(keyValue, inputValue)
    showOutput(outputValue)

root = Tk()
root.title('Cipher')
root.geometry('905x505')
root.resizable(0,0)

Label(root, text='Choose Cipher:').place(x=5, y=5)
cipher = StringVar(root, 'X')
Radiobutton(root, text='Vigenere Cipher Standard', variable=cipher, value='Vigenere Cipher Standard', command=showCipher).place(x=90, y=5)
Radiobutton(root, text='Full Vigenere Cipher', variable=cipher, value='Full Vigenere Cipher', command=showCipher).place(x=90, y=25)
Radiobutton(root, text='Auto-key Vigenere Cipher', variable=cipher, value='Auto-key Vigenere Cipher', command=showCipher).place(x=90, y=45)
Radiobutton(root, text='Extended Vigenere Cipher', variable=cipher, value='Extended Vigenere Cipher', command=showCipher).place(x=260, y=5)
Radiobutton(root, text='Playfair Cipher', variable=cipher, value='Playfair Cipher', command=showCipher).place(x=260, y=25)
Radiobutton(root, text='Affine Cipher', variable=cipher, value='Affine Cipher', command=showCipher).place(x=260, y=45)

# isFile = BooleanVar(root, False)
btnImport = Button(root, text='Import File', command=importFile, bg='grey85', width=8)
btnImport.place(x=460, y=40)

keyLabel = Label(text='Key')
key = Entry(root, width=60)
mKeyLabel = Label(text='M-Key')
mKey = Spinbox(root, from_=1, to=25, width=20)
bKeyLabel = Label(text='B-Key')
bKey = Spinbox(root, from_=1, to=25, width=20)
btnClearKey = Button(root, text='Clear Key', command=clearKey, fg='red', bg='grey85', width=8)

labelInput = Label(text='Plain Text:')
labelInput.place(x=5, y=105)
btnClearText = Button(root, text='Clear Text', command=clearText, fg='red', bg='grey85', width=8)
btnClearText.place(x=5, y=125)
textInput = Text(root, height=10, width=100)
textInput.place(x=90, y=105)

encrypt = BooleanVar(root, True)
btnSwap = Button(root, text='Change to Decrypt', command=swapFunction, bg='grey85')
btnSwap.place(x=90, y=285)
btnConvert = Button(root, text='Convert', command=convertText, bg='grey85')
btnConvert.place(x=210, y=285)

outputType = StringVar(root,'No Spaces')
labelChoose = Label(root, text="Choose Output: ")
labelChoose.place(x=280, y=285)
btnNoSpace = Radiobutton(root, text='No Spaces', variable=outputType, value='No Spaces', command=typeOutput)
btnNoSpace.place(x=370, y=285)
btnN5Letter = Radiobutton(root, text='n-5 Letter', variable=outputType, value='n-5 Letter', command=typeOutput)
btnN5Letter.place(x=470, y=285)

canSave = BooleanVar(root, True)
btnSave = Button(root, text='Save To Json File', command=saveToJsonFile, bg='grey85')
btnSave.place(x=675, y=285)
btnDownload = Button(root, text='Download Json File', command=downloadJsonFile, bg='grey85')
btnDownload.place(x=780, y=285)

labelOutput = Label(root, text='Cipher Text:')
labelOutput.place(x=5, y=330)
textOutput = Text(root, height=10, width=100, state=DISABLED)
textOutput.place(x=90, y=330)

mainloop()