alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',' ']

#morseToAlphabet takes in a morse encoded message and returns the decrypted english message
def morseToAlphabet(message): 
    translation = "";
    message = message.split("   ")
    
    for i in range(len(message)):
        word = message[i].split()
        for j in range(len(word)):
            for k in range(len(morse)):
                if (word[j]==morse[k]):
                    translation += alphabet[k]
        translation += " "

    return translation.lstrip(" ")

#alphabetToMorse takes in a english decrypted message and returns an encrypted morse message
def alphabetToMorse(message):
    translation = " "
    message = message.lower().split()

    for i in range(len(message)):
        for j in range(len(message[i])):
            for k in range(len(alphabet)):
                #print((message[i])[j])
                if (((message[i])[j]) == alphabet[k]):
                    translation += morse[k]
            translation += " "
        translation += "   "

    return translation.lstrip(" ")

#printOut displays an alphabet : morse chart to help out users
def printOut():
    block = ("------------------------")
    for i in range(26):
        print(alphabet[i] + " : " + morse[i])
    print(block)


def menu():
    run = 1
    choice = ""
    block = ("------------------------")
    print("Hello there and welcome to the pyDotDash Morse/English translator!\n")
    while(run==1): 
        print("Would you like to...") 
        print("See an Alphabet : Morse [C]hart")
        print("Write a message in [M]orse")
        print("Write a message [E]nglish?")
        print("or e[X]it?")
        print(block)
        choice = input("").upper()
        if (choice == "C"):
            printOut()

        elif (choice == "M"):
            print("How would you like to enter your message?\n")
            print("1) [K]eyboard")
            inputMethod = input("").upper()

            print ("How would you like to output your message?\n")
            print("1) [C]onsole")
            outputMethod = input("").upper()

            if (inputMethod == "K"):
                print("Please enter your message: (Format is one space between characters and three spaces between words)")
                morseMessage = input("")
                englishMessage = morseToAlphabet(morseMessage)

                if (outputMethod == "C"): 
                    print("Your translated message is: ")
                    print(englishMessage)

            print("Would you like to run pyDotDash again? ([Y]/[N])")
            repeat = input("").upper()

            if (repeat == "Y"):
                print("")

            elif (repeat =="N"):
                print("EXITING PROGRAM")
                run = 0
            else:
                print("INVALID ENTRY DETECTED, EXITING PROGRAM")
                run = 0




        elif (choice == "E"):
            print("How would you like to enter your message?\n")
            print("1) [K]eyboard")
            inputMethod = input("").upper()

            print("How would you like to output your message?\n")
            print("1) [C]onsole")
            outputMethod = input("").upper()

            if (inputMethod == "K"):
                print("Please enter your message: ")
                englishMessage = input("")
                morseMessage = alphabetToMorse(englishMessage)

                if (outputMethod == "C"): 
                    print("Your translated message is: ")
                    print(morseMessage)

            print("Would you like to run pyDotDash again? ([Y]/[N])")
            repeat = input("").upper()

            if (repeat == "Y"):
                print("")

            elif (repeat =="N"):
                print("EXITING PROGRAM")
                run = 0
            else:
                print("INVALID ENTRY DETECTED, EXITING PROGRAM")
                run = 0


        elif (choice == "X"):
            print("EXITING PROGRAM")
            quit()

        else:
            print("Invalid entry, please choose one of the options mentioned")
    




#Sample Messages for Testing Purposes
msg = "HELLO THERE!"
mmsg = ".... . .-.. .-.. ---   - .... . .-. ."

#printOut()
#morseToAlphabet(mmsg)
#print("- - - - - - - - -")
#alphabetToMorse(msg)

menu()
