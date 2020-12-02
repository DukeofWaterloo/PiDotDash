from playsound import playsound as ps
import time

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.','?',';',':','/','-',"'",'"','(',')','=','+','*','@']

morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','--..--','.-.-.-','..--..','-.-.-.','---...','-..-.','-....-','.----.','-...-','-.--.','-.--.-','-...-','.-.-.','-..-','.--.-.']

dot = './audio/dot.mp3'
dash = './audio/dash.mp3'

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

#alphabetToMorseBeep takes in an encrypted morse message and beeps it out to the user
def alphabetToMorseBeep(message):
    for i in range(len(message)):
        if (message[i] == "."):
            ps(dot)
        elif (message[i] == "-"):
            ps(dash)
        else:
            time.sleep(0.2)
    print("")

#alphabetToMorseBeepSpecial takes in an encrypted morse messsage and both types as well as beeps it out to the user
def alphabetToMorseBeepSpecial(message):
    for i in range(len(message)):
        if (message[i] == "."):
            print(".", end='', flush=True)
            ps(dot)
        elif (message[i] == "-"):
            print("-", end='', flush=True)
            ps(dash)
        else:
            print(" ", end='', flush=True)
            time.sleep(0.2)
    print("")

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
    print("Hello there and welcome to the PiDotDash Morse/English translator!\n")
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

        elif (choice == "M"): #INPUTTING MORSE OUTPUTTING ENGLISH
            print("How would you like to enter your message?\n")
            print("1) [K]eyboard")
            inputMethod = input("").upper()
            inputValid = 0

            if (inputMethod == "1"):
                inputMethod = "K"

            if (inputMethod == "K"):
                inputValid = 1

            while (inputValid == 0):
                print("Invalid entry detected, please enter a valid option!")
                inputMethod = input("").upper()
                if (inputMethod == "1"):
                    inputMethod = "K"

                if (inputMethod == "K"):
                        inputValid = 1

            print ("How would you like to output your message?\n") 
            #print("(To combine options take the sum of their numbers, ie. [C]onsole + [S]peech = 3)")
            print("1) [C]onsole")
            #print("2) [S]peech")
            outputMethod = input("").upper()
            outputValid = 0

            if (outputMethod == "1"):
                outputMethod = "C"
            
            if (outputMethod == "2"):
                outputMethod = "B"

            if (outputMethod == "C" or outputMethod == "B"):
                outputValid= 1

            while (outputValid == 0):
                print("Invalid entry detected, please enter a valid option!")
                outputMethod = input("").upper()
                if (outputMethod == "1"):
                    outputMethod = "C"
                if (outputMethod == "2"):
                    ouputMethod = "B"

                if (outputMethod == "C" or outputMethod == "B"):
                    outputValid = 1

            if (inputMethod == "K"):
                print("Please enter your message: (Format is one space between characters and three spaces between words)")
                morseMessage = input("")
                englishMessage = morseToAlphabet(morseMessage)

            if (outputMethod == "C"): 
                print("Your translated message is: ")
                print(englishMessage)

            elif (outMethod == "B"):
                print("Your translated message is: ")


            print("Would you like to run PiDotDash again? ([Y]/[N])")
            repeat = input("").upper()

            if (repeat == "Y"):
                print("")

            elif (repeat =="N"):
                print("Thank you for using PiDotDash!\nEXITING PROGRAM")
                run = 0
            else:
                print("INVALID ENTRY DETECTED, EXITING PROGRAM")
                run = 0




        elif (choice == "E"): #INPUTTING ENGLISH OUTPUTTING MORSE
            print("How would you like to enter your message?\n")
            print("1) [K]eyboard")
            inputMethod = input("").upper()
            inputValid = 0

            if (inputMethod == "1"):
                inputMethod = "K"

            if (inputMethod == "K"):
                inputValid = 1

            while (inputValid == 0):
               print("Invalid entry detected, please enter a valid option!")
               inputMethod = input("").upper()
               if (inputMethod == "1"):
                   inputMethod = "K"

               if (inputMethod == "K"):
                   inputValid = 1

            print("How would you like to output your message?\n") 
            print("(To combine options take the sum of their numbers, ie. [C]onsole + [B]eeps = 3)")
            print("1) [C]onsole")
            print("2) [B]eeps")
            outputMethod = input("").upper()
            outputValid = 0

            if (outputMethod == "1"):
                outputMethod = "C"

            if (outputMethod == "2"):
                outputMethod = "B"

            if (outputMethod == "C" or outputMethod == "B" or outputMethod == "3"):
                outputValid = 1

            while (outputValid == 0):
               print("Invalid entry detected, please enter a valid option!")
               outputMethod = input("").upper()
               if (outputMethod == "1"):
                   outputMethod = "C"
               if (outputMethod == "2"):
                   outputMethod = "B"

               if (outputMethod == "C" or outputMethod == "B" or outputMethod == "3"):
                   outputValid = 1

            if (inputMethod == "K"):
                print("Please enter your message: ")
                englishMessage = input("")
                morseMessage = alphabetToMorse(englishMessage)

            if (outputMethod == "C"): 
                print("Your translated message is: ")
                print(morseMessage)

            elif (outputMethod == "B"):
                print("Your translated message is: ")
                alphabetToMorseBeep(morseMessage)

            elif (outputMethod == "3"):
                print("Your translated message is: ")
                alphabetToMorseBeepSpecial(morseMessage)
                        

            print("Would you like to run PiDotDash again? ([Y]/[N])")
            repeat = input("").upper()

            if (repeat == "Y"):
                print("")

            elif (repeat =="N"):
                print("Thank you for using PiDotDash!\nEXITING PROGRAM")
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
#msg = "HELLO THERE!"
#mmsg = ".... . .-.. .-.. ---   - .... . .-. ."

ps(dot)
ps(dash)
menu()

