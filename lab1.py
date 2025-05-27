import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        return []

print(solve_quadratic(1, -3, 2))