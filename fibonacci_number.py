num = int(input("Enter nth fibonacci number: "))


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(num)

print(result)
