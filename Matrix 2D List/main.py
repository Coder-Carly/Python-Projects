m=[["a","b","c"], [1,2,3], ["d","e","f"],[4,5,6]]
print(m)

#number of rows
print(len(m))

#number of columns
print(len(m[0]))

r=len(m)
c=len(m[0])

for i in range(0,r):
    for j in range (0,c):
        print(m[i][j],end="  ")
    print("\n")

mat=[]
row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))

for x in range(0,row):
    temp=[]
    for y in range(0,col):#
        val=input("Enter the item you want to add: ")
        temp.append(val)
    mat.append(temp)

for i in range(0,row):
    for j in range(0,col):
        print(mat[i][j], end="  ")
    print("\n")
