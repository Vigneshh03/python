for _ in range(1000): 
    num1 = int(input("Enter first number (-1 to stop): "))
    if num1 == -1:
        break
    num2 = int(input("Enter second number (-1 to stop): "))
    if num2 == -1:
        break 
    print(f"Product: {num1 * num2}")
