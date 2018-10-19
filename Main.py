from gtts import gTTS
import os
def profile():
  print("what do you want to edit")
  f = open(filename,"wt")
  username = str(username)
  age = input("how old are you")
  color = input("what is your favourite color")
  food = input("what is your favourite food")
  jokes = input("do you like jokes 1=yes, 2=no")
  intelligence = input("how smart are you")
  f.write('{}\n{}\n{}\n'.format(username,age,color))
  f.close()
print("hi I am your personal assistant sonia")
print("plese if you do not have a profile make a .txt file named (username).txt")
username = input("type your username")
filename = str(username + ".txt")
directory = input(" type 1 if your profile is not setup yet, type 2 if your profile is set up")
if directory == ("1"):
  f = open(filename,"wt")
  username = str(username)
  age = input("how old are you")
  color = input("what is your favourite color")
  food = input("what is your favourite food")
  jokes = input("do you like jokes 1=yes, 2=no")
  intelligence = input("how smart are you")
  f.write('{}\n{}\n{}\n'.format(username,age,color))
  f.close()
if directory == ("2"):
  f = open(filename, "r")
  lines = f.readlines()
  name = (lines[0])  # or whatever you want to do with 
  if name == ("hunter") or name == ("Hunter"):
    print("hi " + name + " My name is sonia, I am your personal assistant, maybe we could blow up North Korea")
  else:
    print("hi " + name + " My name is sonia, I am your personal assistant")
    tts = gTTS(text="hi " + name + " My name is sonia, I am your personal assistant", lang="en")
    tts.save("introduction.mp3")
    os.system("mpg321 introduction.mp3")
  while True:
    todo = input("what can I help you with?, type 1 = help")
    if todo == ("nuke korea") or todo == ("0"):
      print("comoing soon")
    if todo == ("help") or todo == ("1"):
      Help = open("help.txt", "r")
      print(Help.read())
      if name == ("hunter") or name == ("Hunter"):
        print("0-nuke Korea")
    if todo == ("time") or todo == ("2"):
      ("coming soon")
    if todo == ("math") or todo == ("3"):
      print("coming soon")
    if todo == ("password generator") or todo == ("4"):
      print("coming soon")
    if todo == ("profile") or todo == ("5"):
      profile()
    if todo == ("chat") or todo == ("6"):
      print("coming soon")
    if todo == ("credits") or todo == ("7"):
      print("credit to Hunter Harrison, Ethan Mederios, Connor Madden & Rohith Mohan")
      credit = input("type the first name of the person who you want to learn about")
      if credit == ("Hunter") or credit == ("hunter"):
        print("coming soon")
      if credit == ("Ethan") or credit == ("ethan"):
        print("coming soon")
      if credit == ("Connor") or credit == ("connor"):
        print("coming soon")
      if credit == ("Rohith") or credit == ("rohith"):
        print("coming soon") 
    
  
    
    


    

f.close()

