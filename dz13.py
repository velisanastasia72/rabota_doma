import math

def calculate_area(figure_type, **params):

    if figure_type == 'rhombus':
        d1 = params.get('d1')
        d2 = params.get('d2')
        if d1 is None or d2 is None:
            return 'invalid data'
        return (d1 * d2) / 2

    elif figure_type == 'square':
        c = params.get('c', params.get('a'))
        if c is None:
            return 'invalid data'
        return c ** 2

    elif figure_type == 'trapezoid':
        a = params.get('a')
        b = params.get('b')
        h = params.get('h')
        if a is None or b is None or h is None:
            return 'invalid data'
        return 0.5 * (a + b) * h

    elif figure_type == 'circle':
        r = params.get('r')
        if r is None:
            return 'invalid data'
        return math.pi * r ** 2

    else:
        return 'invalid data'


print(calculate_area('rhombus', d1=10, d2=8)) 
print(calculate_area('square', a=5))
print(calculate_area('trapezoid', a=12, b=3, h=6))
print(calculate_area('circle', r=18))
print(calculate_area('unknown', a=1, b=2, c=3))