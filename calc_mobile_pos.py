from sympy import Eq, symbols, solve

# this function is for the distance calculation

def calc_mobile_pos(cord1,cord2,cord3):
    x,y=symbols('x y')
    eq1 = Eq((x - int(cord1[0])) ** 2 + (y - int(cord1[1])) ** 2 - int(cord1[2]) ** 2,0)
    eq2 = Eq((x - int(cord2[0])) ** 2 + (y - int(cord2[1])) ** 2 - int(cord2[2]) ** 2,0)
    eq3 = Eq((x - int(cord3[0])) ** 2 + (y - int(cord3[1])) ** 2 - int(cord3[2]) ** 2,0)
    sol = solve((eq1,eq2,eq3),(x,y))
    x = sol[0][0]
    y = sol[0][1]
    return x,y

print(calc_mobile_pos((0,1,1),(0,-1,1),(1,0,1)))

