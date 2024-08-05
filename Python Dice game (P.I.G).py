import random
import time

print("Welcome to the game of P.I.G")
time.sleep(1)
print("In this game a six sided dice will be rolled and whatever number it lands on will be your score")
time.sleep(1)
print("In this game if you roll a 1 your score will be reset to a zero.")
time.sleep(1)
print("To roll the dice again presss the y key, if you wish to end your turn the you press any other key")
time.sleep(1)
print("After this another players turn will begin, whoever reaches a score above 50 is the winner")
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input ("Enter the number of players(2-4): ")
    
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
    else: print("Invalid, try again")

