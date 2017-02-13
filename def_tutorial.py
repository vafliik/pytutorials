def fib_limit(limit: int):
    a, b = 0,1
    while a < limit:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib_count(count: int):
    a, b = 0, 1
    for _ in range(count):
        print(a, end=' ')
        a, b = b, a + b
    print()

to_call = fib_limit
to_call(10)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword