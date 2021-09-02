from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from extendedVigenereCipher import encryptEVC, decryptEVC
from playfairCipher import encryptPfC, decryptPfC
from affineCipher import invMod, encryptAfnC, decryptAfnC

def showCipher():
  if cipher.get() == 6:
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

def importFile():
  # file = filedialog.askopenfile()
  # print(file)
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

def showOutput(outputValue):
  if (cipher.get() != 4):
    temp = outputValue.replace(" ", "")
    outputValue = [outputValue[i:i+5] for i in range(0, len(outputValue), 5)]
    outputValue = ' '.join(outputValue)
  textOutput.config(state=NORMAL)
  textOutput.delete('1.0', END)
  textOutput.insert(tkinter.END, outputValue)
  textOutput.config(state=DISABLED)

def convertText():
  if cipher.get() == 0:
    tkinter.messagebox.showinfo('Error', 'Cipher type not selected')
  elif textInput.get('1.0', 'end-1c') == '':
    tkinter.messagebox.showinfo('Error', 'No input available')
  elif cipher.get() != 6 and key.get() == '':
    tkinter.messagebox.showinfo('Error', 'No key available')
  elif cipher.get() == 6 and (mKey.get() == '' or bKey.get() == ''):
    tkinter.messagebox.showinfo('Error', 'No M-key or B-key available')
  elif cipher.get() == 6:
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
    if (cipher.get != 4):
      inputValue = ''.join(filter(str.isalpha, textInput.get('1.0', 'end-1c'))).upper()
      keyValue = ''.join(filter(str.isalpha, key.get())).upper()
    else:
      inputValue = textInput.get('1.0', 'end-1c')
      keyValue = key.get()

    if cipher.get() == 1:
      outputValue = 'Belum dibuat'
    elif cipher.get() == 2:
      outputValue = 'Belum dibuat'
    elif cipher.get() == 3:
      outputValue = 'Belum dibuat'
    elif cipher.get() == 4:
      if encrypt.get():
        outputValue = encryptEVC(keyValue, inputValue)
      else:
        outputValue = decryptEVC(keyValue, inputValue)
    elif cipher.get() == 5:
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
cipher = IntVar()
Radiobutton(root, text='Vigenere Cipher standard', variable=cipher, value=1, command=showCipher).place(x=90, y=5)
Radiobutton(root, text='Full Vigenere Cipher', variable=cipher, value=2, command=showCipher).place(x=90, y=25)
Radiobutton(root, text='Auto-key Vigenere Cipher', variable=cipher, value=3, command=showCipher).place(x=90, y=45)
Radiobutton(root, text='Extended Vigenere Cipher', variable=cipher, value=4, command=showCipher).place(x=260, y=5)
Radiobutton(root, text='Playfair Cipher', variable=cipher, value=5, command=showCipher).place(x=260, y=25)
Radiobutton(root, text='Affine cipher', variable=cipher, value=6, command=showCipher).place(x=260, y=45)

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

labelOutput = Label(root, text='Cipher Text:')
labelOutput.place(x=5, y=330)
textOutput = Text(root, height=10, width=100, state=DISABLED)
textOutput.place(x=90, y=330)

# x = Label(root)
# x.place(x=600, y=5)
# y = Label(root)
# y.place(x=600, y=25)

mainloop()