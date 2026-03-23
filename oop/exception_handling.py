#exception handling

#example
'''
num = int(input("Enter a number: "))
print(10/num)
this gives ZeroDivisionError so
'''

#solution
print("----exception handling---")
try:
   print('inside try except block')
   num = int(input("Enter a number: "))
   print(10/num)
except :
   print("Invalid input")


#exceptio handling with specific error
print("----exception handling with specific error---")
try:
   print('inside try except block')
   num = int(input("Enter a number: "))
   print(10/num)
except ValueError :
   print("Invalid input.Please enter a number")   # enter string
except ZeroDivisionError:
   print("You can't divide by zero")


#else and finally
print("----exception handling with else and finally---")
try:
   x = 10/ 2
except ZeroDivisionError:
   print("You can't divide by zero")
else:
   print("success",x)
finally:
   print("this always runs and works ")


#user defined exception to handle the error and provide more usability and flexibilty
print("----user defined exception---")
'''
def withdraw(balance, amount):
   if amount > balance:
       raise Exception('Not enough funds or insufficient balance USER DEFINED')
   return balance - amount

withdraw = withdraw(100, 100987)
print(withdraw)
#this gives error below is another method
'''

#custom exception
print("----custom exception---")
class InsufficientBalanceError(Exception):
   pass

def withdraw(balance, amount):
   if amount > balance:
       raise InsufficientBalanceError('Not enough funds or insufficient balance CUSTOM')

withdraw = withdraw(1000,100)
print(withdraw)


#Real life example
#login
def login(username, password):
   if username != "admin" :
       raise ValueError("User not found")
   if password != "1234" :
       raise ValueError("Wrong Password ")
   return "Into login "

try:
   print(login("admin", "1234"))
   # print(login("kdjhfdk", "1234"))
   # print(login("admin", "34343"))
except ValueError as e:
   print(e)
