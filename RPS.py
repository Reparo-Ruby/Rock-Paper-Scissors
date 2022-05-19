import random

def game_welcome():
    print("""Welcome to Rock, Paper, Scissors.
In this game you have three round to try and win agains your opponet whom is the computer.
In cases of a tie a round is not lost and neither of you get a point.
                            LET THE GAMES BEGIN
    """)


def player_guess():
    userhand = input("Pick your fighter, [R]ock, [P]aper, [S]cissor.\n")
    return userhand


def check_guess(user_guess):
    
    if user_guess == "R":
        user_guess = "Rock"
        return user_guess

    elif user_guess == "P":
        user_guess = "Paper"
        return user_guess

    elif user_guess == "S":
        user_guess = "Scissor"
        return user_guess

    else:
        invalid_input()
        return False


def evaluate_rock(computer,rounds,userhand2):

    if userhand2 == "Rock":
        rounds -=1
        if computer == "Paper":
            print("Paper beats Rock!\n")
            return True
        elif computer == "Scissor":
            print("Rock beats Scissor!\n")
            return False
        elif computer == "Rock":
            rounds += 1
            print("Its A Tie!\n")
    return rounds   


def evaluate_paper(computer,rounds,userhand2):

    if userhand2 == "Paper":
        rounds -=1
        if computer == "Rock":
            print("Paper beats Rock!\n")
            return True
        elif computer == "Scissor":
            print("Scissor beats Paper!\n")
            return False
        elif computer == "Paper":
            rounds += 1
            print("Its A Tie!\n")
    return rounds        
            

def evaluate_scissor(computer,rounds,userhand2):

    if userhand2 == "Scissor":
        rounds -=1
        if computer == "Paper":
            print("Scissor beats Paper!\n")
            return True
        elif computer == "Rock":
            print("Rock beats Scissor!\n")
            return False
        elif computer == "Scissor":
            rounds += 1
            print("Its A Tie!\n")
    return rounds 


def who_wins(computer,player):

    print(f"""GAME RESULTS
{computer}:{player}""")
    
    if computer > player:
        print("Your Opponent Won!")
    elif computer < player:
        print("You Win!!")


def invalid_input():

    input = """******************************************************
Game only understands [R]ock, [P]aper,[S]cissors.
******************************************************"""
    print(input)
    return 
    

def evaluate_responses(computer_pick,computer_wins,user_wins):

    rounds = 3

    while rounds != 0:
        computer = random.choice(computer_pick)
        userhand2 = check_guess(player_guess())

        if userhand2 == False:
            break

        if evaluate_rock(computer,rounds,userhand2):
            if True:
                user_wins +=1
            continue
        
        elif evaluate_paper(computer,rounds,userhand2):
            if True:
                user_wins +=1
            continue

        elif evaluate_scissor(computer,rounds,userhand2):
            if True:
                user_wins +=1
            continue
    
        else:
            computer_wins += 1

        return computer_wins,user_wins    
        
          
def run_game():
    hands = ["Rock","Paper","Scissor"]
    game_welcome()
    com,you = evaluate_responses(hands,0,0)
    who_wins(com,you)


if __name__ == "__main__":
    run_game()
