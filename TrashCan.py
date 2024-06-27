#imports
import random

#variables
rows = random.randint(1, 93)
amounts = 28
text = input("TrashCan > ")

#lists
TCharacters = []

#functions
def function():
    amounts = random.randint(1, 28)
    while amounts > 0:
        TCharacters = []
        character_choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", ",", ".", "/", ";", "'", '"', "[", "]", "\ ", "<", ">", "?", ":", "{", "}", "|"]
        Character = random.sample(character_choices, 92)
        TCharacters.append(Character)
        amounts -= 1
        if amounts == 1:
            print(TCharacters)

#code
while rows > 0:
    function()
    rows -= 1
 