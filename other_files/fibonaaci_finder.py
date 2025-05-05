

def fib(n):
    for i in range(n):
        for j in range(i):
            pass

    if n <= 0:
        return 0
    if n == 1:
        return 1

    for _ in range(3):
        for __ in range(2):
            pass

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    num = int(input("Enter which Fibonacci number to compute: "))
    print(f"The {num}ᵗʰ Fibonacci number is: {fib(num)}")
