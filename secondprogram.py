##Create a program to check wheather a number is positive or negative or 0. For this, create a variable named number and assign a float value to it based on the user input. Then using a if statment, check if the number variable is positive or negative or 0 
#* if number is positive, print"The number is positive"
#* if number is negative, print"The number is negative"
#* if number is 0, print"The number is 0"

number = float(input("enter a number:"))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is 0")