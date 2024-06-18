import os
import random

#Tic-tac-Toe Table

R1 = ['1','2','3']
l1 = ['-----------']
R2 = ['4','5','6']
l2 = ['-----------']
R3 = ['7','8','9']


#Variables

turn_variable = 0

#Checks if someone has won

def checkwin():   
    if R1[0] == R1[1] == R1[2]:
        if R1[0] == 'X':
            print("\nCongrats, Player Won!")
            return True
        else:
            print("\nComputer Won!")
            return True
    elif R2[0] == R2[1] == R2[2]:
        if R2[0] == 'X':
            print("\nCongrats, Player Won!")
            return True
        elif R2[0] == 'O':
            print("\nComputer Won!")
            return True
    elif R3[0] == R3[1] == R3[2]:
        if R3[0] == 'X':
            print("\nCongrats, Player Won!")
            return True
        elif R3[0] == 'O':
            print("\nComputer Won!")
            return True
    elif R1[0] == R2[0] == R3[0]:
        if R1[0] == 'X':
            print('\nPlayer Won')
            return True
        elif R1[0] == 'O':
            print("\nComputer won")
            return True
    elif R1[1] == R2[1] == R3[1]:
        if R1[1] == 'X':
            print('\nPlayer Won')
            return True
        elif R1[1] == 'O':
            print("\nComputer won")
            return True
    elif R1[2] == R2[2] == R3[2]:
        if R1[2] == 'X':
            print('\nPlayer Won')
            return True
        elif R1[2] == 'O':
            print("\nComputer won")
            return True
    elif R1[0] == R2[1] == R3[2]:
        if R1[0] == 'X':
            print('\nPlayer Won')
            return True
        elif R1[0] == 'O':
            print("\nComputer won")
            return True
    elif R1[2] == R2[1] == R3[0]:
        if R1[2] == 'X':
            print('\nPlayer Won')
            return True
        elif R1[2] == 'O':
            print("\nComputer won")
            return True

#Prints the board

def PrintBoard():  
    print(R1)
    print(l1)
    print(R2)
    print(l2)
    print(R3)

#Checks for turn

def whoseturn():
    global turn_variable
    turn_variable += 1
    
    if turn_variable % 2 == 1:
        return 1
    else:
        return 0

#checks if move is new or it has been already played (This avoids repetation of moves)

def movevalidation(move):
    if move == 1:
        if R1[0] == '1':
            return True
        else:
            return False
    elif move == 2:
        if R1[1] == '2':
            return True
        else:
            return False
    elif move == 3:
        if R1[2] == '3':
            return True
        else:
            return False
    elif move == 4:
        if R2[0] == '4':
            return True
        else:
            return False
    elif move == 5:
        if R2[1] == '5':
            return True
        else:
            return False
    elif move == 6:
        if R2[2] == '6':
            return True
        else:
            return False
    elif move == 7:
        if R3[0] == '7':
            return True
        else:
            return False
    elif move == 8:
        if R3[1] == '8':
            return True
        else:
            return False
    elif move == 9:
        if R3[2] == '9':
            return True
        else:
            return False
        
# Makes the move 

def makemove(move, player):
    if move == 1:
        R1[0] = player
    elif move == 2:
        R1[1] = player
    elif move == 3:
        R1[2] = player
    elif move == 4:
        R2[0] = player
    elif move == 5:
        R2[1] = player
    elif move == 6:
        R2[2] = player
    elif move == 7:
        R3[0] = player
    elif move == 8:
        R3[1] = player
    elif move == 9:
        R3[2] = player

os.system('cls')
print("=======================")
print("Welcome to tick-tac-toe")
print("=======================")
print("=======================")
print("===== Player = X =====")
print("==== Computer = Y ====")
print("=======================")
input("Press Enter to Continue")


# Basic code starts here! 

while True:
    PrintBoard()
    gameover = checkwin()
    if gameover == True:
        break
    os.system('cls')
    PrintBoard()
    val = whoseturn()

    if val == 1:
        #Its player turn
        while True:
            player_move = input("\nYour Turn (1-9): ")
            
            if player_move.isdigit():
                player_move = int(player_move)

                if 0 < player_move < 10:
                    move_valid = True
                else:
                    print("Please enter number B/w 1 and 9")
                    continue
            else:
                print("Please Enter Digits Only! ")
                continue

            is_move_new = movevalidation(player_move)

            if is_move_new is True and move_valid is True :
                makemove(player_move,"X")
                break
            else:
                continue
    else:
        #its Computers turn
        while True:
            comp_move = random.randint(1,9)
            is_valid = movevalidation(comp_move)

            if is_valid is True:
                makemove(comp_move,"O")
                break
            else:
                continue