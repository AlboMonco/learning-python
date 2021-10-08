import random
def rps():
    play_again = True
    while play_again:
        player_input = input("Paper [p], Rock [r] or Scissors [s]?")
        if player_input.lower() not in ["r", "p", "s"]:
            print ("Invalid move.")
            continue

        if player_input == "r":
            player_input = "Rock"
            computer_input = "Paper"
        elif player_input == "p":
            player_input = "Paper"
            computer_input = "Scissors"
        elif player_input == "s":
            player_input = "Scissors"
            computer_input = "Rock"

        print ("You selected {} and computer selected {}. Computer wins!\n".format(player_input, computer_input))

        play_again = bool(int(input("Want to play again? Yes [1] or No [0].")))


def rockps():
    play_again = True
    while play_again:
        player_choice = int(input("Paper[1],Rock[2],Scissors[3]"))
        if player_choice not in [1,2,3]:
            print("Invalid move")
            continue
        computer_choice = random.randint(1,3)
        choices ={1:"Paper",2:"Rock",3:"Scissors"}
        win_choices = {1:2,2:3,3:1}
        lost_choices = {1:3,2:1,3:2}
        for i in range(3):
            if [player_choice,computer_choice] == [list(win_choices.keys())[i],list(win_choices.values())[i]]:
                print("You won!")
                break
            if [player_choice,computer_choice] == [list(lost_choices.keys())[i],list(lost_choices.values())[i]]:
                print("You lost")
                break
            else:
                print("Draw")
        print ("You selected {} and computer selected {}.".format([player_choice],list(choices.values())[computer_choice]))
        play_again = bool(int(input("Want to play again? Yes[1] or No[0].")))
        
        
        

 
            
 
            

















            
if __name__ == "__main__":
    rps()
