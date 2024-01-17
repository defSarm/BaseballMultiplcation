from multiprocessing.connection import wait
from time import sleep
from random import randint
from playsound import playsound

# POINT TABLE
Hitting_Table = ("""
Hitting Table
24 - 36 | HOME RUN
18 - 23 | TRIPLE
11 - 17 | DOUBLE
0 - 10  | SINGLE
""")

# SCORE BOARD
#p1
s1w = 0
s2w = 0
s3w = 0
tot1 = s1w + s2w + s3w
#p2
s1p = 0
s2p = 0
s3p = 0
tot2 = s1p + s2p + s3p

board = (f"Player 1| {s1w} | {s2w} | {s3w} | {tot1} | \n \
Player 2| {s1p} | {s2p} | {s3p} | {tot2} |")


print(board)
print(Hitting_Table)

playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Opening.mp3')

print("Welcome to Baseball Multiplcation!")
print("Pick your team color")
print("""
Blue
Red
Green
Orange
""")


#Player1 chooses a color
while True:
    color1 = input("Player 1 Color: ").upper()
    if color1.isalpha and len(color1) != 0:
        if color1 == "BLUE" or color1 == "RED" or color1 == "GREEN" or color1 == "ORANGE":
            print(f"Player 1 choose {color1}")
            break
    else:
        print("Doesn't work, Try again")
      

#Player2 chooses a color
while True:
    color2 = input("Player 2 Color: ").upper()
    if color2.isalpha and color2 != color1 and len(color2) != 0:
        if  color2 == "BLUE" or color2 == "RED" or color2 == "GREEN" or color2 == "ORANGE":
            print(f"Player 2 choose {color2}")
            break
    else:
        print("Doesn't work / Color already choosen / Empty space")

print(f"""P1: {color1}
P2: {color2}""")

print("Player 1 you're up")
sleep(1)
print(Hitting_Table)
strike = 0
outs = 0
plates = 3
round = 1
player = 1
while True:
    out = randint(1, 5)
    if out == 3:
        if outs == 3:
            continue
        else:
            print("You're out!")
            playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Out.mp3')
            outs += 1
            sleep(2)
            continue
    elif strike < 3 and outs < 3:
        num1 = randint(1, 12)
        num2 = randint(1, 3)
        product = str(num1*num2)
        equation = str(input(f"{num1} x {num2} = "))
        if product == equation:
            if int(product) >= 0 and int(product) <= 10:
                print("A solid single")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Single.mp3')
                sleep(1)
                if plates >= 1:
                    plates = plates-1
                    print("plates: " + str(plates))
                elif plates == 0:
                    if player == 1 and round == 1:
                        s1w += 1
                    elif player == 1 and round == 2:
                        s2w += 1
                    elif player == 1 and round == 3:
                        s3w += 1
                    elif player == 2 and round == 1:
                        s1p += 1
                    elif player == 2 and round == 2:
                        s2p += 1
                    elif player == 2 and round == 3:
                        s3p += 1
                    print("plates: " + str(plates))
            elif int(product) >= 11 and int(product) <= 17:
                print("Good hitting, a double!")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Double.mp3')
                sleep(1)
                if plates >= 2:
                    plates = plates-1
                    print("plates: " + str(plates))
                elif plates == 0:
                    if player == 1 and round == 1:
                        s1w += 2
                    elif player == 1 and round == 2:
                        s2w += 2
                    elif player == 1 and round == 3:
                        s3w += 2
                    elif player == 2 and round == 1:
                        s1p += 2
                    elif player == 2 and round == 2:
                        s2p += 2
                    elif player == 2 and round == 3:
                        s3p += 2
                    plates += 1
                    print("plates: " + str(plates))
                elif plates == 1:
                    if player == 1 and round == 1:
                        s1w += 1
                    elif player == 1 and round == 2:
                        s2w += 1
                    elif player == 1 and round == 3:
                        s3w += 1
                    elif player == 2 and round == 1:
                        s1p += 1
                    elif player == 2 and round == 2:
                        s2p += 1
                    elif player == 2 and round == 3:
                        s3p += 1
                    print("plates: " + str(plates))
            elif int(product) >= 18 and int(product) <= 23:
                print("Alright, A triple!")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Triple.mp3')
                sleep(1)
                if plates == 3:
                    plates = plates-1
                    print("plates: " + str(plates))
                elif plates == 0:
                    if player == 1 and round == 1:
                        s1w += 3
                    elif player == 1 and round == 2:
                        s2w += 3
                    elif player == 1 and round == 3:
                        s3w += 3
                    elif player == 2 and round == 1:
                        s1p += 3
                    elif player == 2 and round == 2:
                        s2p += 3
                    elif player == 2 and round == 3:
                        s3p += 3
                    plates += 2
                    print("plates: " + str(plates))
                elif plates == 1:
                    plates += 1
                    if player == 1 and round == 1:
                        s1w += 2
                    elif player == 1 and round == 2:
                        s2w += 2
                    elif player == 1 and round == 3:
                        s3w += 2
                    elif player == 2 and round == 1:
                        s1p += 2
                    elif player == 2 and round == 2:
                        s2p += 2
                    elif player == 2 and round == 3:
                        s3p += 2
                    print("plates: " + str(plates))
                elif plates == 2:                
                    if player == 1 and round == 1:
                        s1w += 1
                    elif player == 1 and round == 2:
                        s2w += 1
                    elif player == 1 and round == 3:
                        s3w += 1
                    elif player == 2 and round == 1:
                        s1p += 1
                    elif player == 2 and round == 2:
                        s2p += 1
                    elif player == 2 and round == 3:
                        s3p += 1
                    print("plates: " + str(plates))
            elif int(product) >= 24 and int(product) <= 36:
                print("It is outta here!")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\HomeRun.mp3')
                sleep(1)
                if plates == 3:
                    if player == 1 and round == 1:
                        s1w += 1
                    elif player == 1 and round == 2:
                        s2w += 1
                    elif player == 1 and round == 3:
                        s3w += 1
                    elif player == 2 and round == 1:
                        s1p += 1
                    elif player == 2 and round == 2:
                        s2p += 1
                    elif player == 2 and round == 3:
                        s3p += 1
                    print("plates: " + str(plates))
                elif plates == 2:
                    if player == 1 and round == 1:
                        s1w += 2
                    elif player == 1 and round == 2:
                        s2w += 2
                    elif player == 1 and round == 3:
                        s3w += 2
                    elif player == 2 and round == 1:
                        s1p += 2
                    elif player == 2 and round == 2:
                        s2p += 2
                    elif player == 2 and round == 3:
                        s3p += 2
                    plates += 1
                    print("plates: " + str(plates))
                elif plates == 1:
                    if player == 1 and round == 1:
                        s1w += 3
                    elif player == 1 and round == 2:
                        s2w += 3
                    elif player == 1 and round == 3:
                        s3w += 3
                    elif player == 2 and round == 1:
                        s1p += 3
                    elif player == 2 and round == 2:
                        s2p += 3
                    elif player == 2 and round == 3:
                        s3p += 3
                    plates += 2
                    print("plates: " + str(plates))
                elif plates == 0:
                    if player == 1 and round == 1:
                        s1w += 4
                    elif player == 1 and round == 2:
                        s2w += 4
                    elif player == 1 and round == 3:
                        s3w += 4
                    elif player == 2 and round == 1:
                        s1p += 4
                    elif player == 2 and round == 2:
                        s2p += 4
                    elif player == 2 and round == 3:
                        s3p += 4
                    plates += 3
                    print("plates: " + str(plates))
        else:
            strike += 1
            if strike == 1:
                print("Strike 1!")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Strike1.mp3')
            elif strike == 2:
                print('Strike 2!')
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Strike2.mp3')
            else:
                print('Strike 3!')
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Strike3.mp3')
            sleep(2)
            continue


    elif strike == 3 or outs == 3:
        if player == 1 and round < 4:
            plates = 3
            strike = 0
            outs = 0
            player = 2
            tot1 = s1w + s2w + s3w
            tot2 = s1p + s2p + s3p
            board = (f"Player 1| {s1w} | {s2w} | {s3w} | {tot1} | \n \
Player 2| {s1p} | {s2p} | {s3p} | {tot2} |")
            print(board)
            playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\NextRoundMusic.mp3')
            print("Ok player 2, lets see what you've got!")
            if color2 == "GREEN":
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Green.mp3')
            elif color2 == "ORANGE":
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Orange.mp3')
            elif color2 == "RED":
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Red.mp3')
            elif color2 == "BLUE":
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Blue.mp3')
        elif player == 2 and round < 4:
            if round == 1:
                print("Thats the end of the 1st inning!")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\1stInning.mp3')
                plates = 3
                strike = 0
                outs = 0
                player = 1
                round = 2
                tot1 = s1w + s2w + s3w
                tot2 = s1p + s2p + s3p
                board = (f"Player 1| {s1w} | {s2w} | {s3w} | {tot1} | \n \
Player 2| {s1p} | {s2p} | {s3p} | {tot2} |")
                print(board)
                sleep(2)
                print('Ok Player 1, its your turn')
                if color2 == "GREEN":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Green.mp3')
                elif color2 == "ORANGE":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Orange.mp3')
                elif color2 == "RED":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Red.mp3')
                elif color2 == "BLUE":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Blue.mp3')
            elif round == 2:
                print("Thats the end of the 2nd inning!")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\2ndInning.mp3')
                plates = 3
                strike = 0
                outs = 0
                player = 1
                round = 3
                tot1 = s1w + s2w + s3w
                tot2 = s1p + s2p + s3p
                board = (f"Player 1| {s1w} | {s2w} | {s3w} | {tot1} | \n \
Player 2| {s1p} | {s2p} | {s3p} | {tot2} |")
                print(board)
                sleep(2)
                print("Player 1, Lets see what you've got")
                if color2 == "GREEN":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Green.mp3')
                elif color2 == "ORANGE":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Orange.mp3')
                elif color2 == "RED":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Red.mp3')
                elif color2 == "BLUE":
                    playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\Blue.mp3')
                elif round == 3:
                    print("Thats the ball game!")
                playsound('C:\\Users\\samantha\\Downloads\\Programming\\Python\\Baseball Multiplcation\\BaseballAudio\\End.mp3')
                tot1 = s1w + s2w + s3w
                tot2 = s1p + s2p + s3p
                board = (f"Player 1| {s1w} | {s2w} | {s3w} | {tot1} | \n \
Player 2| {s1p} | {s2p} | {s3p} | {tot2} |")
                print(board)
                if tot1 > tot2:
                    print(f"{color1} team won!")
                elif tot2 > tot1:
                    print(f"{color2} team won!")
                elif tot1 == tot2:
                    print("A tie game!")
                sleep(2)
                break

    print()

print("Thanks for playing!")
exit = input("> ")