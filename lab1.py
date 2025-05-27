import math

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
        return
    
    b = get_valid_number("b = ")
    c = get_valid_number("c = ")
    
    solutions = solve_quadratic(a, b, c)
    print(format_solutions(solutions))

interactive_mode()