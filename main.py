# Function that adds two numbers
def add(x,y) :
    print(x+y)


x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))


# Function that subtract two numbers
def subtract(x,y) :
    print(x-y)


x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))


# Function that multiply two numbers
def multiply(x,y) :
    print(x*y)


x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))


# Function that divide two numbers
def divide(x,y) :
    print(x/y)


x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))



#######################################################
####### Start of program
print("Welcome to mah awsome calc app!")
print("What would you like to do?")
print("Type (a)dd (s)ubtract (m)ultiply (d)ivde (q)uit")

while True:

    user_choice = input(": ")
    #print(user_choice)
    x = int(input("Enter your first name:  "))
    y = int(input("Enter your second number: "))


    if user_choice == 'a' :
            add(x,y)

    elif user_choice == 's' :
            sub(x,y)

    elif user_choice == 'm' :
            mul(x,y)

    elif user_choice == 'd' :
            div(x,y)1

    elif user_choice == 'q' :
        break;
    else:
        print("Invalid choice")

    if (x,y) == (8,9):
        print ("89!")