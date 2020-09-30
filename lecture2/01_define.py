

def hello_n(name: str, n: int):
    for i in range(n):
        print("Привет,", name + "!")

hello_n('Вася', 5)
hello_n('Петя', 3)


vasya = 'Вася', 3

print('\n')

hello_n(*vasya)
