from cmath import exp
from operator import index
import os
from re import I
import string
import sys
from tabnanny import check

from numpy import array

wordlist = open("words.txt","r")
words = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
checkedWrongLetters =[]
wrongSpot = {}
correctSpot = [""]*5

for line in wordlist:
  stripped_line = line.strip()
  words.append(stripped_line)
save = words

def wordParser(input: string):
  finalArr = [""]*5
  entry = input.lower()
  if len(entry)==5:
    for i in range(0,len(entry)):
      if entry[i] in letters:
        finalArr[i] = entry[i]
    print("Valid String")
    return finalArr
  else:
    print("Invalid String")

def addWrongLetters(entry: array):
  wrongWords = set()
  for letter in entry:
    if (letter in letters) and (letter not in checkedWrongLetters):
      checkedWrongLetters.append(letter)
      for word in words:
        if letter in word:
          wrongWords.add(word)
  wrongWords = sorted(wrongWords)
  #print (wrongWords)
  for i in wrongWords:
    words.remove(i)

def addWrongSpot(entry:array):
  wrongWords = set()
  for idx in range(0,5):
    letter = entry[idx]
    if letter not in checkedWrongLetters:
      if letter in wrongSpot:
        wrongSpot[letter].append(idx)
      else:
        wrongSpot[letter] = [idx]
    for i in words:
      if letter not in i:
        wrongWords.add(i)
      if i[idx]== letter:
        wrongWords.add(i)
  wrongWords = sorted(wrongWords)
  for i in wrongWords:
    words.remove(i)

def addCorrectLetters(entry:array):
  wrongWords = set()
  for idx in range(0,5):
    letter = entry[idx]
    if letter in letters:
      for i in words:
        if (i[idx] is not letter):
          wrongWords.add(i)
  wrongWords = sorted(wrongWords)
  for i in wrongWords:
    words.remove(i)

def undo():
  words = save

def menu():
  status = True
  while status:
    selection = int(input("1. Take Round\n2. Look At Possible Words\n3. Undo\n4. Exit\n"))
    if selection ==4:
      status = False
    elif selection ==2:
      print (words)
    elif selection == 1:
      save = words
      entry = None
      while entry == None:
        entry = wordParser(input("Enter the wrong letters, GREY, with dashes (-) separating letters that are not red ex. (cr-a-e)\n"))
      addWrongLetters(entry)
      entry = None
      while entry ==None:
        entry = wordParser(input("Enter the correct letters in wrong spots, YELLOW, with dashes (-) separating letters that are not red ex. (cr-a-e)\n"))
      addWrongSpot(entry)
      entry = None
      while entry ==None:
        entry = wordParser(input("Enter the correct letters in correct spots, GREEN, with dashes (-) separating letters that are not red ex. (cr-a-e)\n"))
      addCorrectLetters(entry)
    elif selection == 3:
      undo()
    else:
      print("Invalid Selection")


#menu()
