words = set()

print("Enter words (type 'stop' to finish)")

while True:
    word=input("Enter word: ").lower()
    if word=="stop":
        break
    if word in words:
        print("Duplicate ignored!")
    else:
        words.add(word)
        print("Added!")

print("\n Unique words collected: ")
print(words)