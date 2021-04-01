from gtts import gTTS
from playsound import playsound 

Message = input("Enter The Message/Text: ")
speech = gTTS(text = Message)
m = input("enter the file name with .mp3:")
speech.save(m)
cmd = input("Enter yes/no to play the file: ")
if (cmd=="yes" or cmd=="Yes"):
    playsound(m)
else:
    pass