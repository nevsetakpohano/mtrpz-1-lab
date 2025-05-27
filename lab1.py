import math
import sys

def get_valid_number(prompt):
    while True:
        try:
            value = input(prompt).strip()
            num = float(value)
            return num
        except ValueError:
            print(f"Error. Expected a valid real number, got '{value}' instead")

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [round(x1, 2), round(x2, 2)]
    elif discriminant == 0:
        x = -b / (2*a)
        return [round(x, 2)]
    else:
        return []

def format_solutions(solutions):
    if not solutions:
        return "There are 0 roots"
    if len(solutions) == 1:
        return f"There is 1 root\nx1 = {solutions[0]:.1f}"
    return f"There are 2 roots\nx1 = {solutions[0]:.1f}\nx2 = {solutions[1]:.1f}"

def validate_file_content(content):
    lines = content.strip().split('\n')
    if len(lines) != 1:
        return False
    parts = lines[0].split()
    if len(parts) != 3:
        return False
    try:
        float(parts[0])
        float(parts[1])
        float(parts[2])
    except ValueError:
        return False
    return True

def interactive_mode():
    print("Interactive mode. Enter coefficients:")
    a = get_valid_number("a = ")
    if a == 0:
        print("Error: 'a' cannot be zero")
        sys.exit(1)
    
    b = get_valid_number("b = ")
    c = get_valid_number("c = ")
    
    print(f"Equation is: ({a:.1f}) x^2 + ({b:.1f}) x + ({c:.1f}) = 0")
    solutions = solve_quadratic(a, b, c)
    print(format_solutions(solutions))

def noninteractive_mode(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            if not validate_file_content(content):
                print("Error. Invalid file format. Expected single line with 3 real numbers separated by spaces.")
                sys.exit(1)
            
            coefficients = content.strip().split()
            a = float(coefficients[0])
            if a == 0:
                print("Error: 'a' cannot be zero")
                sys.exit(1)
            
            b = float(coefficients[1])
            c = float(coefficients[2])
            
            print(f"Equation is: ({a:.1f}) x^2 + ({b:.1f}) x + ({c:.1f}) = 0")
            solutions = solve_quadratic(a, b, c)
            print(format_solutions(solutions))
            
    except FileNotFoundError:
        print(f"Error. File '{file_path}' does not exist")
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        noninteractive_mode(sys.argv[1])
    else:
        print("Usage:")
        print("  Interactive mode: python equation.py")
        print("  Non-interactive mode: python equation.py filename.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()