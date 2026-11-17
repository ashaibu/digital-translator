def calculate(first_number, operator, second_number):

    if operator == "multiply":
        return first_number * second_number 

    if operator == "divide": 
        if second_number == 0:
            return "cannot divide by zero"

        return first_number / second_number
    
    if operator == "add":
        return first_number + second_number 

    if operator == "subtract":
        return first_number - second_number

    return "Invalid operator."
