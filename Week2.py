# print("Please think of a number between 0 and 100!")
# guess = 50
# lb=0
# hb=100
# c=''
# while (c != 'c'):
#     print("Is your secret number ", guess, "?", sep='')
#     c = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
#     if c == 'h': hb=guess; guess=int(guess-(hb-lb)/2)
#     elif c == 'l': lb=guess; guess=int(guess+(hb-lb)/2)
#     elif (c!= 'c'): print("Sorry, I did not understand your input.")
# print("Game over. Your secret number was",guess)
#
#
# def a(x, y, z):
#     if x:
#         return y
#     else:
#         return z
#
#
# def b(q, r):
#     return a(q > r, q, r)
#
# a(3>2,a,b)
#
#
# def gcdIter(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#     value = min(a, b)
#     while (a % value != 0) or (b % value != 0):
#         if value == 1: break
#         value -= 1
#     return (value)


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 1:
        if aStr != char:
            return (False)
        else:
            return (True)
    if aStr[len(aStr)//2] > c:
        return (isIn(char, astr[:len(aStr) // 2]))
    else:
        return (isIn(char, astr[len(aStr) // 2:]))

print(isIn('s','eekllmmopqqrsuwyzzzz'))

aStr = 'eekllmmopqqrsuwyzzzz'

aStr[len(aStr)//2]

import pandas as pd
import numpy as np

df = pd.read_csv("stocksdata.csv",  delim_whitespace=True, header=None, index_col=None).T
df.columns=df.iloc[0,0:10]
df=df.drop(df.index[0])
df=df.reset_index(drop=True)
df.head()
print(df.columns)

df['CAL'][1]

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
z = ['_'] * len(secretWord)
for i in range(len(secretWord)):
    if secretWord[i] in lettersGuessed: z[i] = secretWord[i]
return (''.join(z))

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

def EuclidGCD(a,b):
    if b==0:
        return(a)
    return EuclidGCD(b,a%b)

print(EuclidGCD(357,234))