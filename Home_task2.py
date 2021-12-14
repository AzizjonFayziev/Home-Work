signs = {
   'add': '+',
   'substract': '-', 
}

def calc (a, b, action):
    return eval(f'{a}{signs.get(action)}{b}')
print(calc(2, 3, 'add'))
print(calc(2, 3, 'substract'))