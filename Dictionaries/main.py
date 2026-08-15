capital = {'India':'New Delhi', 'USA':'Washington DC', 'France':'Paris', 'Sri Lanka':'Colombo'} #creation of dictionary
print(capital['India'])
capital['UK']='London' #adding a new key & value to the dictionary
print(capital['UK']) #checking the key & value are there
print(capital) #printing the whole dictionary
print(capital.keys()) #printing just the keys of the dictionary
print(capital.values()) #printing just the values of the dictionary
print(len(capital)) #printing the length of the dictionary
print('USA' in capital) #checking whether a certain key is in the dictionary
print('Nigeria' in capital)
del capital ['USA'] #deleting a key & value in the dictionary
print(capital) #checking whether it has been deleted
capital['Sri Lanka'] = 'Salkjsjkfjajjefijwajd' #changin an already existed value in the dictionary
print(capital) #checking whether it's been changed
countries=[]  #making the keys into a list
for i in capital:
    countries.append(i)

print(countries)
countries.sort() #sorting the list
print(countries)