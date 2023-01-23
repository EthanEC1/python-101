import random

while True:
    my_answer = input("Choose: rock, paper, or scissors... ")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break
    
    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print("must answer: rock, paper, or scissors")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    
    print(f"computer chose: {computer_answer}")

    if computer_answer == my_answer:
        print("tie")
        continue
    elif my_answer == "paper" and computer_answer == "rock":
        print("Player wins")
    elif my_answer == "rock" and computer_answer == "scissors":
        print("Player wins")
    elif my_answer == "scissors" and computer_answer == "paper":
        print("Player wins")
    elif computer_answer == "paper" and my_answer == "rock":
        print("Computer wins")
    elif computer_answer == "rock" and my_answer == "scissors":
        print("Computer wins")
    elif computer_answer == "scissors" and my_answer == "paper":
        print("Computer wins")