#!/usr/bin/python3

letters = {}

userword = input("What word or phrase do you want to analyze?").upper()

for lett in userword:
  if lett in letters.keys():
    letters[lett] += 1
  else:
    letters[lett]=1

for key,value in letters.items():
  print(key + "occurs" + str(value) + "times")


