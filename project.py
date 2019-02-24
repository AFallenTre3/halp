'''
This program will pit a 
physical player against a simple cpu in Rock, Paper, Scissors 
to see who comes out on top 
it was inspired by my group traditionally playing rock paper scissors 
who determined who would put the laptops away at the end of class
'''

# Imports
from random import randint

# cpu randomly picks either rock, paper, or scissors
def rpors():
    
    cpu = randint(1, 3)
    random = "R"
    if cpu == 2:
        random = "P"
    elif cpu == 3:
        random = "S"
    return random

# asks what you want to pick (rock, paper, scissors)
def playerrpors():
    num = input("What will you choose? R/P/S ")
    return num

# recognizes if your pick beats the cpus pick
def beat(num, random):
   t = ""
    
   if num == "R" and random == "S":
       t = "True"
   elif num == "R" and random == "P":
       t = "False"
   elif num == "P" and random == "R":
       t = "True"
   elif num == "P" and random == "S":
       t = "False"
   elif num == "S" and random == "R":
       t = "True"
   elif num == "S" and random == "P":
       t = "False"
   elif num == random:
       t = "ITS A TIE! Play again!"
   return t

def winner(num, random, t):
    if t == "True":
        print("YOU WON! You picked " + num + " they picked " + random)
    elif t == "False":
        print("YOU LOST. You picked " + num + " they picked " + random)
    else:
        print(t)

def main():
    
    player = playerrpors()
    computer = rpors()
    result = beat(player, computer)
    winner(player, computer, result)
    
if __name__ == '__main__':
    while True:
        main()
        y_n = input('Play again? y/n ')
        if y_n.lower() != 'y':
            break
