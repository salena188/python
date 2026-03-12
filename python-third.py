#function in python

def greet():   #defining a function
   print("Hello, Salina") #function body or implementation
#greet()  # calling the function


# function +argument

def test(name):  #function with parameter (name is the parameter)
   print("Hello, " + name)
test("Jagriti")  # calling the function with argument



# function + return types

def add(a, b):  #function with parameters a and b
   return a + b  #returning the sum of a and b    
result = add(5, 3)  # calling the function with arguments and storing the result
print("The sum is:", result)  # printing the result








#file handling in python
#file = open("example.txt", "w")  # opening a file in write mode
#file.write("Hello, this is an example of file handling in Python.")  # writing to the file
#file.close()  # closing the file
'''
w write mode - if the file does not exist, it will be created. If it already exists, it will be overwritten.
r read mode - if the file does not exist, it will raise an error. If it exists, it will be opened for reading.
a append mode - if the file does not exist, it will be created. If it already exists, new data will be added to the end of the file without overwriting the existing content.
'''


#save data to a file
def saveDataToFile():
    file = open("userdata.txt", "a")  # opening a file in append mode
    for i in range(3):  # loop to get data for 3 users
       name = input("Enter your name: ")
       age = input("Enter your age: ")
   # writing to the file
       file.write(f"Name: {name}, Age: {age}\n")  # writing user data to the file
 
    file.close()  # closing the file


saveDataToFile()  # calling the function to save data to the file




def readDataFromFile():
   file = open("userdata.txt", "r")  # opening a file in read mode
   data = file.read()  # reading the content of the file
   print("User Data:\n", data)  # printing the content of the file
   file.close()  # closing the file


readDataFromFile()  # calling the function to read data from the file