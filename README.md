# PiDotDash 
A Raspberry Pi Morse Translator coded in Python which offers users a variety of ways to enter a message in either Morse or English (or any language which uses the same 26 letters as the English alphabet) and encodes their message in the opposite format.

As of right now the current I/O options are as follows:

|  | Morse | English |
| --- | --- | --- |
| Input | Keyboard | Keyboard |
| Output | Console <br> Text to Speech (Beep) | Console <br> Text to Speech | 

In addition to the above methods of I/O, I am planning to add the following too!

|  | English | Morse |
| --- | --- | --- |
| Input | Speech to Text <br> From a File | Physical Button <br> Speech (Beep) to Text ? |
| Output | | Blinking LED | 

The following PyPI packages _might_ be needed to run this program: [playsound](https://pypi.org/project/playsound/) and [pyttsx3](https://pypi.org/project/pyttsx3/)
