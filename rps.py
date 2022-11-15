from random import randrange

computer = randrange(3)
''' 
0 = rock
1 = scissors
2 = paper
'''
game = False
'''game_start = raw_input("Would you like to play a game? y/n: ")

if game_start == "y":
    game == True
elif game_start == "n":
    exit
else:
    print("Please input a valid response")
    game_start = raw_input("Would you like to play a game? y/n: ")'''
    
while game == False: 
    game_start = raw_input("Would you like to play a game? y/n: ")

    if game_start == "y":
        game = True
    elif game_start == "n":
        break
    else:
        print("Please input a valid response")
    
    


while game ==  True:
    player = str(raw_input("Chose rock(r), paper(p), or scissor(s): "))

    if player == "r" and computer == 0:
        print("It's a draw!")
        print("I had a rock\n")

        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")

    elif player == "s" and computer == 0:
        print("You lost:(")
        print("I had a rock\n")

        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")

    elif player == "p" and computer == 0:
        print("You won:)")
        print("I had a rock\n")
        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")
            
    elif player == "r" and computer == 1:
        print("You won:)")
        print("I had scissors\n")

        cont= raw_input("Would you like to continue? y/n ")
        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")
            
    elif player == "s" and computer == 1:
        print("It's a draw!")
        print("I had scissors\n")

        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")
            
    elif player == "p" and computer == 1:
        print("You lost:(")
        print("I had scissors\n")

        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")
            
    elif player == "r" and computer == 2:
        print("You lost:(")
        print("I had paper\n")

        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")
            
            
    elif player == "s" and computer == 2:
        print("You lost:(")
        print("I had paper\n")

        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")
            
    elif player == "p" and computer == 2:
        print("It's a draw!")
        print("I had paper\n")

        cont= raw_input("Would you like to continue? y/n ")

        if cont == "y":
            game = True
        elif cont == "n":
            break
        else:
            print("Please input a valid response")
            


