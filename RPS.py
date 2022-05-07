import random
def game_welcome():
    print("""Welcome to Rock, Paper, Scissors.
In this game you have three round to try and win agains your opponet whom is the computer.
In cases of a tie a round is not lost and neither of you get a point.
                            LET THE GAMES BEGIN
    """)

def who_wins(com,you):
    print(f"""GAME RESULTS
{com}:{you}""")
    
    if com > you:
        print("Your Opponent Won!")
    elif com < you:
        print("You Win!!")

 

def invalid_input():
    input = """******************************************************
Game only understands [R]ock, [P]aper,[S]cissors.
******************************************************"""
    
    return input


def evaluate_responses(computer_pick,c_wins,u_win):
    rounds = 3

    while rounds != 0:
        computer = random.choice(computer_pick)
        userhand = input("Pick your fighter, [R]ock, [P]aper, [S]cissors.\n")
        hand = userhand.upper()

        if hand == "R":
            rounds -=1
            if computer == "Paper":
                print("Paper beats Rock!\n")
                c_wins += 1
            elif computer == "Scissors":
                print("Rock beats Scissors!\n")
                u_win += 1
            elif computer == "Rock":
                rounds += 1
                print("Its A Tie!\n")
            continue

        elif hand == "P":
            rounds -=1
            if computer == "Rock":
                print("Paper beats Rock!\n")
                u_win += 1
            elif computer == "Scissors":
                print("Scissors beats Paper!\n")
                c_wins += 1
            elif computer == "Paper":
                rounds += 1
                print("Its A Tie!\n")
            continue

        elif hand == "S":
            rounds -=1
            if computer == "Paper":
                print("Scissors beats Paper!\n")
                u_win += 1
            elif computer == "Rock":
                print("Rock beats Scissors!\n")
                c_wins += 1
            elif computer == "Scissors":
                rounds += 1
                print("Its A Tie!\n")
            continue
        
        else:
            response = invalid_input()
            print(response)

    return c_wins,u_win
        

def run_game():
    hands = ["Rock","Paper","Scissors"]
    game_welcome()
    com,you = evaluate_responses(hands,0,0)
    who_wins(com,you)

if __name__ == "__main__":
    run_game()
