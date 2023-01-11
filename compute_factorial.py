def compute_factorial(n):
    # Complete this recursive function
    if n <= 0:
        return 1
    return n * compute_factorial(n - 1)


num = int(input())
# Call the compute_factorial function
print(compute_factorial(num))
