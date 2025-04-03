def calculator():
    print("simple calculator")
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
    print("1 => addition \n2 => subtraction \n3 => multiplication \n4 => division ")
    choice = int(input("select 1/2/3/4 :"))
    if choice == 1:
        result = int(num1+num2)
        print(f"addition of {num1} and {num2} is : {result}")
    elif choice == 2:
        result = int(num1-num2)
        print(f"subtractio of {num1} and {num2} is : {num1}-{num2}")
    elif choice == 3:
        result=int(num1*num2)
        print(f"multiplication of {num1} and {num2} is : {result}")
    elif choice == 4:
        if num2 == 0:
            print("divide with zero is not divisable")
            return
        result = num1/num2
        print(f"division of {num1} and {num2} is : {result}")
    else:
        print("your entered choice is incorrect")
calculator()