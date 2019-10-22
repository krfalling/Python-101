#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:57:48 2019

@author: krfalling
"""

high = 100
low = 0
ans = (high + low) // 2

print ("Please think of a number between 0 and 100!")
print ("Is your secret number " + str(ans) + "?")
print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
letter = input ("")

while letter != "c":

    if letter == "h":
        high = ans
        ans = (ans + low) // 2
        print ("Is your secret number " + str(ans) + "?")
        print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        letter = input ("")
        
    elif letter == "l":
        low = ans
        ans = (ans + high) // 2
        print ("Is your secret number " + str(ans) + "?")
        print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        letter = input ("")
    else:  
        print ("Sorry, I did not understand your input.")
        print ("Is your secret number " + str(ans) + "?")
        letter = input ("")

print ("Game over. Your secret number was: " + str(ans))
    
        
