#This program will evaluate the input of characters to determine whether a
#Number has been placed. The user will be prompted for two numbers that will
#Be added together. If one or both inputs are not numbers, the user will 
#Receive an message instead of a compiler error

while True:
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    try: 
        a = int(num1) 
        b = int(num2)
        c = a + b
        print(c)

    except ValueError:
        print("One of your values is incorrect,")
        print("You need to provide numbers for your inputs")



 
