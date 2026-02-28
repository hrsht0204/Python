

def calulator():
    try:
        # Start by getting the first number
        result = float(input("first number: "))
        
        while True:
            # Get the operator
            operator = input("Enter an operator:\n'=' for result: ")
            
            if operator == '=':
                break
            
            # Validate the operator
            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator. Please enter +, -, *, / or =.")
                continue
            
            # Get the next number
            next_number = float(input("next number: "))
            
            # Perform the operation
            if operator == '+':
                result += next_number
            elif operator == '-':
                result -= next_number
            elif operator == '*':
                result *= next_number
            elif operator == '/':
                if next_number == 0:
                    print("Error! Division by zero is not allowed.")
                    continue
                result /= next_number

        # Display the final result
        print(f"The final result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the alulator funtion
calulator()
