import random

rock = '''
    ________
---'     ___)
       (______)
       (_____)
       (____)
----.__(___)  

'''

paper = '''
    _________
---'     _____)______
        (_____________)
        (______________)
        (____________)
----.___(__________)  

'''

scissor = '''
    ________
---'     ___)_______
        (___________)
        (____________)
        (____)
----.___(___)  
'''

game_image = [rock,paper,scissor]
your_choice = int(input("what do you choose? 0 for rock, 1 for paper and 2 for scissor:\n"))
if your_choice >= 3 or your_choice < 0:
    print("you typed wrong number so you lose")
else:
    print(game_image[your_choice])
    hand_signals = random.randint(0,2)
    print("computer choice:")
    print(game_image[hand_signals])
    if your_choice >= 3 or your_choice < 0:
        print("you typed wrong number so you lose")
    elif your_choice == 2 and hand_signals == 0:
        print("you lose")
    elif your_choice == 0 and hand_signals == 2:
        print("you won")
    elif your_choice == 0 and hand_signals == 0:
        print("Draw")
    elif your_choice == 0 and hand_signals == 1:
        print("you lose")
    elif your_choice == 1 and hand_signals == 2:
        print("you lose")
    elif your_choice == 1 and hand_signals == 1:
        print("Draw")
    elif your_choice == 1 and hand_signals == 0:
        print("you won")
    elif your_choice == 2 and hand_signals == 2:
        print("Draw")
    elif your_choice == 2 and hand_signals == 1:
        print("you won")







# if your_choice == 0:
#     print("Draw")
# elif your_choice == 1:
#     print("you lost")
# elif your_choice == 2:
#     print("you win")


