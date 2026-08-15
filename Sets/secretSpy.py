secret_set = {6, 7, 21, 69, 91}
lives = 3

print("Guess the Secret Set Game!")
print("There are 5 numbers in the secret set!")
print("You have 3 lives.")
print("Type 0 to quit. \n")

while lives > 0:
    guess = int(input("Enter a number: "))
    if guess == 0:
        print("You quit the game.")
        break

    if guess in secret_set:
        print("Correct! That number is in the Secret Set!")
    else:
        lives -= 1
        print("Sorry, but that number's not in the Secret Set!")
        print("You have {} lives left".format(lives))

print("\n Game Over!")