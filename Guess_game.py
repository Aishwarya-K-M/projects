import random as rand

choice = rand.randint(1,100)

logo = '''


  /$$$$$$                                                /$$$$$$        /$$   /$$           /$$
 /$$__  $$                                              /$$__  $$      | $$$ | $$          | $$
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$      | $$  \ $$      | $$$$| $$  /$$$$$$ | $$
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      | $$$$$$$$      | $$ $$ $$ /$$__  $$| $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$       | $$__  $$      | $$  $$$$| $$  \ $$|__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$      | $$  | $$      | $$\  $$$| $$  | $$    
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/      | $$  | $$      | $$ \  $$|  $$$$$$/ /$$
 \______/  \______/  \_______/|_______/|_______/       |__/  |__/      |__/  \__/ \______/ |__/
                                                                                               
                                                                                               
                                                                                               

'''
print(logo)
print(choice)
def win( no ):
    if(no < choice and no > 0):
        print("Too low!")
        return 0
    elif(no == choice):
        print("Great! you guessed it right...!")
        return 1
    elif(no <= 100 and no > 0):
        print("Too High!")
        return 0
    else:
        print("Guess within the range!")
        return 0


print("Welcome! Guess the no that is selected to win the game...\n")
print("Hint: The no is within the range of 1 and 100\n")
diff = input("Do you want to play the easy or the difficult level? answer e or d ")
print("\n\n")
end = False


if(diff.lower() == 'e' ):
    print("There are 10 chances for you to guess the no")
    print()
    for i in range(10):
        print(f"There are {10-i} chances\n")
        if(end == True):
            break
        user = int(input("Enter your choice: "))
        if(win(user)):
            end = True
    if(end == False):
        print("You have lost the game! Better luck next time")
    else: 
        print("Hurray! You won!")
elif(diff.lower() == 'd'):
    print("You have 5 chances to guess the no")
    for i in range(5):
        print(f"There are {5-i} chances\n")
        if(end == True):
            break
        user = int(input("Enter your choice: "))
        if(win(user)):
            end = True
    if(end == False):
        print("You have lost the game! Better luck next time")
    else: 
        print("Hurray! You won!")
    

