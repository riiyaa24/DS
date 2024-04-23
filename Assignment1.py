#Q1 - Write a program which contains one function named as Fun().
#That function should display "Hello from fun " on console
def Fun():
    print("Hello from Fun ")


#Q2 - Write a program which contains one function named as ChkNum() which accept one parameter
#as number. If number is even then it should display "Even number " otherwise dispplay "Odd number" on console
def ChkNum(num):
    if(num%2==0):
        print("The number is even")
    else:
        print("The number is odd ")


#Q3 - Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers
def Add(num1, num2):
    res = num1 + num2
    print("Addition of two numbers is ", res)
    return res


#Q4 - write a program which display 5times marvellous on screen
def Marvellous():
    for i in range(5):
        print("Marvellous")


#Q5 - Write a program which display 10 to 1 on screen
def fun():
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("\n")


#Q6 - 
def Chk(num):
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    elif num == 0:
        print("Zero")


#Q7 - write a program which contains one function that accept one number from user and returns true
#if number is divisible by 5 otherwise return false
def div(num):
    if num % 5 == 0:
        print("True")
    else :
        print("False")


#Q8 - write a program which accept number from user and print that number 
#of "*" on screen.
def star(num):
    for i in range(num):
        print("*", end=" ")
    print("\n")


#Q9 - write a program which display first 10 even numbers on screen
def even():
    for i in range(2, 21, 2):
        print(i, end=" ")
    print("\n")


#Q10 - Write a program which accept name from user and display
#length of its name
def length(inpt):
    print(len(inpt))



def main():
    Fun()

    num = int(input("Enter a number to check if it even or odd : "))
    ChkNum(num)

    print("Enter first number for addition : ", end=" ")
    num1 = int(input())
    print("Enter second number : ", end=" ")
    num2 = int(input())
    Add(num1, num2)

    Marvellous()

    fun()

    print("Enter a number to check whether it is positive, negative or zero : ", end=" ")
    num = int(input())
    Chk(num)

    print("Enter a number to check divisibility by 5 : ", end=" ")
    num = int(input())
    div(num)

    print("Enter a number to print same number of stars :  ", end=" ")
    num = int(input())
    star(num)

    print("First 10 even numbers : ", end=" ")
    even()

    print("Enter a name for length : ", end=" ")
    inpt = input()
    length(inpt)    



if __name__ == "__main__":
    main()