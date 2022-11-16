import random
def check_valid_string(user_input):
    """
    
    :param user_input: string character
    :return: lower case valid string
    """
    if user_input[0]=="!":
        return False, "!"
    elif user_input[0] in "rRpPsS":
        # ui = user_input[0]
        return [True, user_input[0].lower()]
    else:
        return [False, user_input[0].lower()]

def rps_input(key):
    """
    :param key: dictionary key
    :return: chars r, p or s
    """
    inp = input(key + ", enter 'r', 'p', or 's' \n")
    return check_valid_string(inp)


def check_valid_int(user_input):
    """
    
    :param user_input: int number
    :return: tuple of true if 1 or 2, false if any other char
    """
    if user_input.isdigit():
        if int(user_input) == 1 or int(user_input) == 2:
            return (True, int(user_input))
        else:
            return False, None
    else:
        return False, None


def message(msg):
    """
    
    :param msg: string message
    :return: print string message
    """
    print(msg)





def rps_winner(u1, u2):
    """
    
    :param u1: r p or s of player 1
    :param u2: r p or s of player 2
    :return: list of boolean, depending on who wins
    """
    winner = [False, False, False]  # [u1,u2, draw]
    if u1 == "r":
        if u2 == u1:
            winner[2] = True
        elif u2 == "s":
            winner[0] = True
        else:
            winner[1] = True
    
    elif u1 == "s":
        if u1 == u2:
            winner[2] = True
        elif u2 == "r":
            winner[1] = True
        else:
            winner[0] = True
    
    else:
        if u1 == u2:
            winner[2] = True
        elif u2 == "r":
            winner[0] = True
        else:
            winner[1] = True
    return winner

def rps_random():
    s = "rps"
    return random.choice(s)

def endgame(exclamation):
    return