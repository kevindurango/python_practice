#FOR LOOP

sum = 0 

for i in range(1, 101):
    sum = sum + i
    
    print("sum from 1 to 100 is:",sum)
    
    
x = 5
y = "John"

print(x, type(x))
print(y, type(y))
 
print(x == 6)

x, y, z = ("orange", "banana", "cherry")
print (x,y,z)

#in collection type: List, Tuple, Dictionary


#ARRAY

fruits = ["apple","banana","cherry"]
fruits.append("orange") 
fruits.insert(1,("kiwi"))
len(fruits)

for x in fruits:
    print(x)
    
print("=========================")
[print(x) for x in fruits]

#FILTERING LIST

newlist = [x for x in fruits]
print("**newlist**")
newlist

newListWithA = [x for x in fruits if "a" in x]
newListWithA


newlist = [x for x in range(10,15)]
newlist

newlist = [x.upper() for x in fruits]
newlist

#SORTING ARRAYS,LISTS

fruits.sort()
print("sorted fruits:",fruits)


thisdict= {
    "Brand": "ford",
    "Model": "Mustang",
    "Year": 1964,
    "Color": ["red","white","black"]
}

print(thisdict["Color"])

                         