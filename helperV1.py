from operator import index
import os
import sys

wordlist = open("words.txt","r")
words = []
letterFreq = {'s': 0.5137989515880358,
'e': 0.5135676842429849,
'a': 0.46176379895158803,
'o': 0.34212149244526674,
'r': 0.32053654024051803,
'i': 0.28977798334875116,
'l': 0.25986740672217085,
't': 0.2540086339808819,
'n': 0.22756706753006475,
'u': 0.19357076780758556,
'd': 0.1890995991366019,
'y': 0.15988282454517422,
'c': 0.15633672525439407,
'p': 0.15564292321924145,
'm': 0.15232809127351218,
'h': 0.1356768424298489,
'g': 0.1267345050878816,
'b': 0.12542399013259328,
'k': 0.1160191181005242,
'f': 0.08595436324390995,
'w': 0.08009559050262104,
'v': 0.05349984582176997,
'z': 0.03345667591736047,
'j': 0.022432932469935246,
'x': 0.022201665124884366,
'q': 0.008633980881899476}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
checkedWrongLetters =[]
wrongSpot = {}
correctSpot = [""]*5

for line in wordlist:
  stripped_line = line.strip()
  words.append(stripped_line)

def addWrongLetter():
  wrongLetters = []
  wrongWords = []
  print("Type exit to leave")
  while True:
    userIn = input("Enter Letter ")
    if userIn == "exit": break
    if (userIn in wrongLetters) or (userIn in checkedWrongLetters) or (userIn not in letters) or (userIn in wrongSpot) or (userIn in correctSpot):
      print("Wrong Input! \n ")
    else:
      wrongLetters.append(userIn)
      print("Inputted \n")
      for i in words:
        if userIn in i:
          wrongWords.append(i)
      for i in wrongWords:
        words.remove(i)
      wrongWords = []
    '''for j in wrongLetters:
      checkedWrongLetters.append(j)
      #print(j)
      if j in i:
        wrongWords.append(i)

        break
      break
  print(wrongWords)
  for i in wrongWords:
    words.remove(i)'''


  

def addCorrectLetterWrongSpot():
  print("Type exit to leave")
  while True:
    wrongWords = []
    letterIn = input("Enter Letter ")
    if letterIn == "exit": break
    while (letterIn in checkedWrongLetters) or (letterIn not in letters) or (letterIn in correctSpot):
      print("Wrong Input! \n ")
      letterIn = input("Enter Letter ")
    indexIn = int(input("Enter Position (1-5)"))
    while indexIn >5 or indexIn<1:
      print("Wrong Index! \n")
      indexIn = int(input("Enter Position (1-5)"))
    if letterIn in wrongSpot:
      wrongSpot[letterIn].append(indexIn)
    else:
      wrongSpot[letterIn] = [indexIn]
    for i in words:
      if letterIn not in i:
        wrongWords.append(i)
      if i[indexIn-1]== letterIn:
        wrongWords.append(i)
    for i in wrongWords:
      words.remove(i)
        

def addCorrectLetter():
  print("Type exit to leave")
  while True:
    wrongWords = []
    letterIn = input("Enter Letter ")
    if letterIn == "exit": break
    while (letterIn in checkedWrongLetters) or (letterIn not in letters) or (letterIn in correctSpot):
      print("Wrong Input! \n ")
      letterIn = input("Enter Letter ")
    indexIn = int(input("Enter Position (1-5)"))
    while indexIn >5 or indexIn<1:
      print("Wrong Index! \n")
      indexIn = int(input("Enter Position (1-5)"))
    if letterIn in wrongSpot:
      wrongSpot[letterIn].pop()
    correctSpot[indexIn-1] = letterIn
    print(f"Current list: {correctSpot}")
    for i in words:
      if i[indexIn-1]!=letterIn:
        wrongWords.append(i)
    for i in wrongWords:
      words.remove(i)

def giveGuess():
  pass
  
def menu():
  status = True
  while status:
    selection = int(input("1. Wrong Letter\n2. Wrong Spot\n3. Right Spot\n4. Print Possible Words\n5. Exit\n"))
    if selection ==5:
      status = False
    if selection == 1:
      addWrongLetter()
    if selection == 2:
      addCorrectLetterWrongSpot()
    if selection ==3:
      addCorrectLetter()
    if selection ==4:
      print(words)


  
#menu()