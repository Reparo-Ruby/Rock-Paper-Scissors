import random
def game_welcome():
    print("")

def play():
    
    hands = ["Rock","Paper","Scissors"]
    computer_pick = random.choice(hands)


    return computer_pick

def who_wins():
    computer_wins = 0
    you_win = 0
    
    return computer_wins,you_win


def evaluate_responses(computer_pick):
    rounds = 3
    c_wins, u_win = who_wins()

    while rounds != 0:
        userhand = input("Pick your fighter, [R]ock, [P]aper, [S]cissors.\n")
        computer = random.choice(computer_pick)
        print(computer)

        rounds -=1
        hand = userhand.upper()

        if hand == "R":
            print(rounds)
            if computer == "Paper":
                c_wins += 1
                print("Paper beats Rock. You Lose!")
            elif computer == "Scissors":
                u_win += 1
                print("Rock beats Scissors. You Win!")
            elif computer == "Rock":
                rounds += 1
                print("Its A Tie!")
            continue

        elif hand == "P":
            print(rounds)
            if computer == "Rock":
                print("Paper beats Rock. You Win!")
                u_win += 1
            elif computer == "Scissors":
                print("Scissors beats Paper. You Lose!")
            elif computer == "Paper":
                rounds += 1
                print("Its A Tie!")
            continue

        elif hand == "S":
            print(rounds)
            if computer == "Paper":
                print("Scissors beats Paper. You Win!")
                u_win += 1
            elif computer == "Rock":
                print("Rock beats Scissors. You Lose!")
            elif computer == "Scissors":
                rounds += 1
                print("Its A Tie!")
            continue
        
        else:
            print(rounds)
            print("******************************************************")
            print("Game only understands [R]ock, [P]aper,[S]cissors.")
            print("******************************************************")
    return r
        

def run_game():
    hands = ["Rock","Paper","Scissors"]
    evaluate_responses(hands)

if __name__ == "__main__":
    run_game()
