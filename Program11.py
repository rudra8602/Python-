#This program uses raise exception to catch certain parameters. 
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

calls = [
    ('*', 4, 4),
    ('O', 20, 5),
    ('x', 3, 3),
    ('ZZ', 3, 3),
    ('a', 1, 1),
    ('B',5,5)
]

for symbol, width, height in calls:
    try:
        box_print(symbol, width, height)
        print()  
    except Exception as err:
        print(f"Error with ({symbol}, {width}, {height}): {err}")
        print()
