x=[12,"hello","python",6538748]
print(x)
my_tuple=(12,"hello","python",6538748)
print(my_tuple)
address=["hogsmeade","street 12","hogswart","england"]

for i in address:
    print(i,end=" ")

city,street,school,country=address
print("\n",city)

nest=(1,2,3,("a","b"),[4,5,6])
print(nest[4][1])

bio=()
n=input("Enter your name: ")
bio=(n, )
print(bio)
d=input("Enter your birthdate: ")
m=input("Enter your birthmonth: ")
y=input("Enter your birhtyear: ")
dob=(d,m,y)
bio=(n,(dob))

print(bio)

clr=input("Enter your favourite colour: ")
bio=(n,(dob),clr)
print(bio)

#values in tuples cannot be changed
bio[2]="blue"
print(bio)