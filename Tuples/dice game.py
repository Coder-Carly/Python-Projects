import random
dice=(1,2,3,4,5,6)
score=0
for r in range(5):
    print("Round ",r+1)
    roll1=random.choice(dice)
    roll2=random.choice(dice)

    rolls=(roll1,roll2)

    total=roll1 + roll2
    print("You rolled: ",rolls)
    print("Your total: ",total)

    if total==7:
        print("Lucky 7!!!")
        score+=1
    elif total==12:
        print("Double Six!!!")
        score+=2
    else:
        print("Better luck next time!")

print("Your final score: ",score)
#Tuples are ordered with index positions 0,1,2 etc.
#Tuples are unchangeable - cannot be changed, replaced or altered