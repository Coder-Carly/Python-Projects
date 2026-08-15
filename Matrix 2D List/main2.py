mat = []

row = int(input("Enter the number of rows (students): "))
col = int(input("Enter the number of columns (subjects): "))

# Build header row: blank cell + subject names
header = [""]
for y in range(col):
    val = input(f"Enter subject {y+1} name: ")
    header.append(val)
mat.append(header)

# Build each student row: student name + their scores
for x in range(row):
    temp = []
    name = input(f"Enter student {x+1} name: ")
    temp.append(name)
    for a in range(col):
        score = input(f"  Enter {name}'s score for {mat[0][a+1]}: ")
        temp.append(score)
    mat.append(temp)

# Print the matrix
for i in range(row + 1):
    for j in range(col + 1):
        print(f"{mat[i][j]:<15}", end="")
    print()