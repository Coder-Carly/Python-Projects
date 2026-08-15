studentID={"Y88STCS1","Y88STCS2","Y88STCS3"} #Set of unique student IDs
fruits=["apple","banana","orange","kiwi","pineapple","watermelon","banana"]
myset=set(fruits) #as soon as we convert the list to a set, all the duplicates are removed and the items are also shuffled
print(studentID)
print(fruits)
print(myset)
myset.add("mango") #adding an item to the set
print(myset)
myset.remove("Cherry") #remove will give error because cherry is not present in the set
myset.discard("cherry") #this will not give any error












