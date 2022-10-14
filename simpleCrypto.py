#Code by SukhoiSuperior
import os
from cryptography.fernet import Fernet
import string

#init list containing alphabet and also encoding type
encoding = 'utf-8'
alph = list(string.printable)
encText = ""

#pre-selection for fernet key
if str(input("Existing Transmisson Key? Yes/No")).lower() == "yes":
    f = Fernet(str(input("Key|>")).encode())
else:
    key1 = Fernet.generate_key()
    f = Fernet(key1)
    print(str(key1, encoding))
print("")

#main function to allow for characters to be converted from STR to DEC INT then into a HEX code. top if is for STR->HEX and bottom is for HEX->STR
def combine(modeLen):
    if str(modeLen) == "short":
        baseText = str(input("|>")).encode()    #getting plaintext
        encText = f.encrypt(baseText)           #fernet encryption
        shortD = ""
        encText = str(encText, encoding)        #removing the pesky b'xxx' from the bytes to a straight string of xxx
        for x in encText:
            decD = alph.index(x)                #finding position of ascii char in alph list
            hexD = str(hex(decD))               #converting decimal to HEX
            finD = str(hexD.lstrip("0x"))       #removing the pesky 0xFF part to leave FF
            if len(finD) == 2:                  #this IF-ELIF part is to add functionality for single char HEX
                shortD = shortD + finD          
            elif len(finD) == 1:
                shortD = shortD + "l" + finD
        print(shortD)

    elif str(modeLen) == "long":                
        baseText = str(input("|>")).encode()    #getting base encrypted text
        longE = ""
        helpE = 0
        baseText = str(baseText)
        hexE = 0
        for y in range(len(baseText)):          #looping through the given HEX data
            if str(baseText[y]) == "l":         #checking if there is a 'l' coming up which signifies the next char being a single char HEX 
                helpE += 1
            else:
                posE = int(alph.index(str(baseText[y]))) 
            if helpE == 2:
                decE = int(hexE, base=16)       #taking a HEX number obtained from encrypted text and converting it from base 16 to DEC
                longE = longE + str(alph[decE]) #adding ascii character of same position to list
                helpE = 0
            elif helpE == 1:
                hexE = int(hexE) + posE         #if first char of HEX number now adding second char
                helpE += 1
                print(hexE)
            elif helpE == 0:
                hexE = posE*10                  #adding first char of HEX number
                helpE += 1
                print(hexE)
        longE = longE.encode()                  #setting the string of fernet encrypted data to bytes

while True:                                     #forever loop for main code
    mode = int(input("Tx/Rx/Tn/Rn 1/2/3/4 "))   #obtaining mode (Tx is encrypt, Rx is decrypt, Tn is encrypt with HEX, Rn is decrypt with HEX)
    if mode == 1:                               #Tx 
        baseText = str(input("|>")).encode()
        encText = f.encrypt(baseText)
        print(str(encText, encoding))
    elif mode == 2:                             #Rx
        baseText = str(input("|>")).encode()
        decText = f.decrypt(baseText)
        print(str(decText, encoding))
    elif mode == 3:                             #Tn
        combine("short")
    elif mode == 4:                             #Rn
        combine("long")
        decText = f.decrypt(longE)
        print(str(decText, encoding))
    print("")                                   #space between last line and new line

