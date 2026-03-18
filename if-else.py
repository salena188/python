#if else condtion explanation
marks = int(input("Enter your marks:"))

marks = int(input("Enter your marks: ")) #taking input from user and converting it to integer (type casting to int)
if marks >= 90 and marks <= 100: #checking if marks is greater than or equal to 90 and less than or equal to 100
   print("Grade: A")
elif marks >= 80 and marks < 90:
   print("Grade: B")
elif marks >= 70 and marks < 80:
   print("Grade: C")
elif marks >= 60 and marks < 70:
   print("Grade: D")
else:    print("Grade: F") 