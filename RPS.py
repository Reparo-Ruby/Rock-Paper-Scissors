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
    
    if user_guess.lower() == "r" or user_guess.lower() == "rock":
        user_guess = "Rock"
        return user_guess

    elif user_guess.lower() == "p" or user_guess.lower() =="paper":
        user_guess = "Paper"
        return user_guess

    elif user_guess.lower() == "s" or user_guess.lower() == "scissor":
        user_guess = "Scissor"
        return user_guess

    else:
        invalid_input()


def evaluate_rock(computer,userhand2):

    if userhand2 == "Rock":
        if computer == "Paper":
            print("Paper beats Rock!\n")
            return False
        elif computer == "Scissor":
            print("Rock beats Scissor!\n")
            return True
        elif computer == "Rock":
            print("Its A Tie!\n")


def evaluate_paper(computer,userhand2):

    if userhand2 == "Paper":
        if computer == "Rock":
            print("Paper beats Rock!\n")
            return True
        elif computer == "Scissor":
            print("Scissor beats Paper!\n")
            return False
        elif computer == "Paper":
            print("Its A Tie!\n")     
            

def evaluate_scissor(computer,userhand2):

    if userhand2 == "Scissor":
        if computer == "Paper":
            print("Scissor beats Paper!\n")
            return True
        elif computer == "Rock":
            print("Rock beats Scissor!\n")
            return False
        elif computer == "Scissor":
            print("Its A Tie!\n")


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
    

def evaluate_wins(computer_pick,computer_wins,user_wins):

    rounds = 3

    while rounds != 0:
        computer = random.choice(computer_pick)
        userhand2 = check_guess(player_guess())
            
        if userhand2 == "Rock":
            rounds -= 1
            wins = evaluate_rock(computer,userhand2)
            if wins == True:
                user_wins += 1

            elif wins == False:
                computer_wins += 1 

            else:
                rounds += 1    
            continue
        
        elif userhand2 == "Paper":
            rounds -= 1
            wins = evaluate_paper(computer,userhand2)
            if wins == True:
                user_wins +=1

            elif wins == False:
                computer_wins += 1

            else:
                rounds += 1        
            continue

        elif userhand2 == "Scissor":
            rounds -= 1
            wins = evaluate_rock(computer,userhand2)
            if wins == True:
                user_wins +=1

            elif wins == False:
                computer_wins += 1

            else:
                rounds += 1    
            continue
    
    return computer_wins,user_wins    
        
          
def run_game():
    hands = ["Rock","Paper","Scissor"]
    game_welcome()
    com,you = evaluate_wins(hands,0,0)
    who_wins(com,you)


if __name__ == "__main__":
    run_game()
