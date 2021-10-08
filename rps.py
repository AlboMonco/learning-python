import random
import time
def rps():
    play_again = True
    while play_again:
        player_choice = int(input("Paper[1],Rock[2],Scissors[3]: "))
        if player_choice not in [1,2,3]:
            print("Invalid move")
            continue
        computer_choice = random.randint(1,3)
        choices ={1:"Paper",2:"Rock",3:"Scissors"}
        win_choices = {1:2,2:3,3:1}
        lost_choices = {1:3,2:1,3:2}
        for i in range(3):
            if [player_choice,computer_choice] == [list(win_choices.keys())[i],list(win_choices.values())[i]]:
                time.sleep(3)
                print("\nYou won!")
                break
            if [player_choice,computer_choice] == [list(lost_choices.keys())[i],list(lost_choices.values())[i]]:
                time.sleep(3)
                print("\nYou lost!")
                break
            if player_choice == computer_choice:
                time.sleep(3)
                print("\nDraw.")
                break
        print ("\nYou selected {} and computer selected {}.".format(choices[player_choice],choices[computer_choice]))
        play_again = bool(int(input("\nWant to play again? Yes[1] or No[0].")))
        
                  
if __name__ == "__main__":
    rps()
