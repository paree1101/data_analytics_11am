a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
select = int(input("Select an operation: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))

if select == 1:
    print("The sum of", a, "and", b, "is", a + b)
elif select == 2:
    print("The difference between", a, "and", b, "is", a - b)
elif select == 3:
    print("The product of", a, "and", b, "is", a * b)
elif select == 4:
    if b != 0:
        print("The quotient of", a, "and", b, "is", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid selection. Please select a valid operation.")