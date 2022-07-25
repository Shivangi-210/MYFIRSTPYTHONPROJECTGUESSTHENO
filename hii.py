import random
no = random.randint(1,9)
c = 0
while c<5:
    g = int(input("Enter a number"))
    if g == no:
        print("YOU WON THE GAME! CONGRATS")
        break
    elif g < no:
        print("Its higher!")

    else:
        print("Its lower!")  
    c+=1
if not c<5:
    print("You lost!")
    