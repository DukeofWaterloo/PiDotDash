alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',' ']

def morseToAlphabet(message): #WORK ON THIS LATERRR
    translation = "";
    message = message.split("   ")
    
    for i in range(len(message)):
        word = message[i].split()
        for j in range(len(word)):
            for k in range(len(morse)):
                if (word[j]==morse[k]):
                    translation += alphabet[k]
        translation += " "

    print(translation)


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

    print(translation)

def printOut():
    block = ("------------------------")
    print(block)
    for i in range(26):
        print(alphabet[i] + " : " + morse[i])
    print(block)

#Sample Messages for Testing Purposes
msg = "HELLO THERE!"
mmsg = ".... . .-.. .-.. ---   - .... . .-. ."

printOut()
morseToAlphabet(mmsg)
print("- - - - - - - - -")
alphabetToMorse(msg)
