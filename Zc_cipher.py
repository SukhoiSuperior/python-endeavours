## This inefficient code is intellectual property of SukhoiSuperior 
## https://github.com/SukhoiSuperior

def Zc_cipher(sentence,cipherText): #Takes a normal english sentence and encypts it
    cipher = cipherText
    returnString,sentence = "",str(sentence) #sets the input to be a string (sanitise your inputs always mate)
    for letter in sentence: #iterates through every character in the sentence one by one
        lowCase = False #initialises lowercase check variable
        if letter.isalpha() == True: #checks if the letter is part of the alphabet or not
            if ord(letter) > 91: lowCase = True #checks if the letter is lowercase and if so changes a boolean variable to True
            position = ord(letter.upper()) - 65 #gets the ascii number for that character, then minuses 65 to get a position for the cipher list
            returnLetter = cipher[position] #gets the new character from the cipher
        else:
            returnLetter = letter #if it is not an alphabet, just keep it in its current state and return it

        if lowCase == True: #checks if the character is supposed to be lowercase
            returnString += returnLetter.lower() #adds the new letter to the variable to be returned but changes it to lowercase
        else: 
            returnString += returnLetter #adds the new capital letter to the variable to be returned
    return returnString # returns the new string


def Zc_decipher(sentence,cipherText): #identical code but now decrypting to plaintext
    cipher = cipherText
    returnString,sentence = "",str(sentence)
    for letter in sentence:
        lowCase = False 
        if letter.isalpha() == True:
            if ord(letter) > 91: lowCase = True
            position = cipher.index(letter.upper()) + 65 #using the <list>.index() to get the position of the letter, then adding to get the ascii value
            returnLetter = chr(position)
        else:
            returnLetter = letter

        if lowCase == True: 
            returnString += returnLetter.lower()
        else: 
            returnString += returnLetter 
    return returnString


def Zc_chat(escChar, capital, cipherText): #set up the two-way conversational mode with custom escape characters and if it should be all in capitals or normal text
    modeIn = 1 #set variable to flip 
    print("conversational mode")
    print("it will switch from cipher [C] to decipher [D] every message")
    print("this is your escape code to exit this mode: " + str(escChar))
    print("you have set capital to " + str(capital))
    while True:
        if modeIn == 1: #if its cipher mode
            sentence = input("[C] > ") #gets sentence type
            if sentence == str(escChar): break #if sentence is escape character break

            if capital == True: #check for capitals
                print(Zc_cipher(sentence,cipherText).upper())
            else:
                print(Zc_cipher(sentence,cipherText))
            modeIn = 0 #flips the variable
        else: #same here but just decipher
            sentence = input("[D] > ")
            if sentence == str(escChar): break

            if capital == True: 
                print(Zc_decipher(sentence,cipherText).upper())
            else:
                print(Zc_decipher(sentence,cipherText))
            modeIn = 1

#this is the moment i stopped trying to write documentation for what the hell im doing

def Zc_customSettings(escChar, capital, cipherText): #settings config for escape characters, uppercase default and cipher
    print("Set escape character for typing modes: ")
    print("Currently set as: " + str(escChar))
    if str(input("Do you wish to change? Y/N")).upper() == "Y":
        escChar = str(input("New escape character: "))

    print("Set uppercase as default for output: ")
    print("Currently set as: " + str(capital))
    if str(input("Do you wish to change? Y/N")).upper() == "Y":
        capital = True
    
    print("Configure ciphertext: ")
    print("Currently set as: ")
    print(str(cipherText))
    if str(input("Do you wish to change? Y/N")).upper() == "Y":
        print("enter a string of 26 uppercase letters divided by spaces")
        cipherText = str(input("")).split()
    
    print("Escape character set to: " + str(escChar))
    print("Uppercase default: " + str(capital))
    print("Ciphertext: ")
    print(cipherText)
    return escChar, capital, cipherText


def Zc_plain(escChar,capital,mode,cipherText): #one-way cipher or decipher
    while True:
        if mode == "cipher":
            sentence = str(input("[C] > "))
            if sentence == str(escChar): break
            if capital == True: sentence = sentence.upper()
            print(Zc_cipher(sentence,cipherText))

        elif mode == "decipher":
            sentence = str(input("[D] > "))
            if sentence == str(escChar): break
            if capital == True: sentence = sentence.upper()
            print(Zc_decipher(sentence,cipherText))

def Zc_menu(): #main function
    escChar,capital,cipherText = "|||",False, ['E', 'J', 'I', 'W', 'F', 'H', 'G', 'R', 'N', 'C', 'T', 'D', 'X', 'A', 'Y', 'L', 'Z', 'U', 'O', 'V', 'M', 'S', 'P', 'B', 'Q', 'K']
    while True:
        print()
        print("MENU")
        print("configure settings and ciphertext: 1")
        print("enter conversational mode: 2")
        print("enter cipher mode: 3")
        print("enter decipher mode: 4")
        choice = int(input("choice: "))
        if choice == 1:
            escChar, capital, cipherText = Zc_customSettings(escChar,capital,cipherText)
        elif choice == 2:
            Zc_chat(escChar,capital,cipherText)
        elif choice == 3:
            Zc_plain(escChar,capital,"cipher",cipherText)
        elif choice == 4:
            Zc_plain(escChar,capital,"decipher",cipherText)

Zc_menu()