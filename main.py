import helper as h
import random


def main():
    msg = h.message
    rps_in = h.rps_input
    valid_int = h.check_valid_int
    
    msg("Welcome! type 1 to play with another player or type 2 to play with computer, or ! to end game")
    inp = input()
    if inp == "!":
        print("game ending")
        return
    
    # bool = h.check_valid_int(inp)[0]
    boole = valid_int(inp)
    while not boole:
        inp = input("wrong, type again ")
        boole = valid_int(inp)[0]  # now we are sure inp is either 1 or 2
    
    inp = valid_int(inp)[1]
    dict = {  # i would use a list but wanted to practice dictionaries
        0: "Player 1",
        1: "Player 2",
        2: "computer"}
    u1_score = 0
    u2_score = 0
    draw = 0
    
    # main game
    
    while u1_score < 3 and u2_score < 3:
        
        u1 = rps_in(dict[0])
        if u1[1] == "!":
            print("game ending")
            return
        
        while u1[1] not in "rps":
            msg("wrong! type again")
            u1 = rps_in(dict[0])
        
        if inp == 1: # user vs user
            u2 = rps_in(dict[1])
            if u2[1] == "!":
                print("game ending")
                return
            while u2[1] not in "rps":
                msg("wrong! type again")
                u2 = rps_in(dict[1])
        
        elif inp == 2: # user vs computer
            u2 = h.rps_random()
            print("Player 2: ", u2)
        
        if u1 == "! " or u2 == "!":
            return
        
        winner = h.rps_winner(u1, u2)
        
        if winner[0]:
            msg(dict[0] + " wins\n")
            u1_score += 1
            msg("Player 1 Score: " + str(u1_score))
            msg("Player 2 Score: " + str(u2_score))
        elif winner[1]:
            u2_score += 1
            msg(dict[1] + " wins\n")
            msg("Player 1 Score: " + str(u1_score))
            msg("Player 2 Score: " + str(u2_score))
        elif winner[2]:
            draw += 1
            msg("draw!\n")
            msg("Player 1 Score: " + str(u1_score))
            msg("Player 2 Score: " + str(u2_score))


main()
yn = input("play again? y/n: ")
while yn not in "yn":
    yn = input("play again? y/n: ")
if yn == "y":
    main()
else:
    print("end")
