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
        return f"There is 1 root: x1 = {solutions[0]:.1f}"
    return f"There are 2 roots: x1 = {solutions[0]:.1f}, x2 = {solutions[1]:.1f}"

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
            content = file.read().strip()
            a, b, c = map(float, content.split())
            
            if a == 0:
                print("Error: 'a' cannot be zero")
                sys.exit(1)
                
            print(f"Equation is: ({a:.1f}) x^2 + ({b:.1f}) x + ({c:.1f}) = 0")
            solutions = solve_quadratic(a, b, c)
            print(format_solutions(solutions))
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        noninteractive_mode(sys.argv[1])

if __name__ == "__main__":
    main()