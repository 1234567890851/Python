while True:
    print("\nChoose operstion:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Exiting calculator.")
        break
    
    num1 = float(input("enter first number: "))
    
    num2 = float(input("enter second number: "))
    
    if choice == '1':
        print(f"Result: " ,  (num1 + num2))
    elif choice == '2':
        print(f"Result: ", (num1 - num2))
    elif choice == '3':
        print(f"Result: ", (num1 * num2))
    elif choice == '4':
        if num2 ==0:
            print("error")
        else:
            print(f"Result: ", (num1 / num2))
    else:
        print("invalid")
            