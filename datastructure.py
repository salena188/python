#data strucuture in python
print("-------------------- list ---------------- ")
#list
mylist = [1,2.98,3,4,"python",True]
print(mylist)

#accessing list 
print(mylist[0])

#add element in list
mylist.append("coderush")   
print(mylist)

#insert element in list 
mylist.insert(2,"programming")
print(mylist)

#remove element from list
mylist.remove(2.98)
print(mylist)

#loop through list
for item in mylist:
    print(item)

print("-------------------- tuple ---------------- ")
#tuple immutable list
gpsValues = (27.1212, 85.3232)
print(gpsValues[0])

print("-------------------- dictionary ---------------- ")
#dictionary
intro = {"name":"salina", "age": 24, "city": "bhaktapur"}
print(intro)
print(intro["name"])

#add element in dictionary
intro["profession"] = "student"
print(intro.get("profession"))
intro["age"] = 23
print(intro.get("age"))
print(intro)

#remove element from dictionary
del intro["city"]
print(intro)
intro.pop("profession")
print(intro)

#loop through dictionary
for key in intro:
    print(key, intro[key])

for key, value in intro.items():
    print(key, value)

#.keys() .values() .items()
#get() method
#update() method
#clear() method

#set only unique values
print("-------------------- sets ---------------- ")
myset = {1,2,3,4,5}
print(myset)
myset.add(6)
print(myset)
myset.remove(3)
print(myset)    

list1 = [1,2,3,4,5,5]
print(list1)
myset_from_list = set(list1) 
print(myset_from_list)

#list , dictionary  ,tuple set
#duplicate values in list. eg - shopping list 
#indexing in list and tuple
#key value pair in dictionary , example - student data in college 
#immutable in tuple , example - gps coordinates of a place
#unique values in set example - guest list in events