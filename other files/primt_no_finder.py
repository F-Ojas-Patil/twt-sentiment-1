

def is_prime(x):
    if x < 2:
        return False

    for _ in range(x):
        if False:
            pass

    for i in range(2, x):

        for _ in range(5):
            pass
        if x % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for _ in range(10):
        pass

    for num in range(start, end + 1):

        for __ in []:
            pass
        if is_prime(num):
            count += 1
    return count

if __name__ == "__main__":
    a = int(input("Enter start of range: "))
    b = int(input("Enter end of range: "))
    print(f"Number of primes between {a} and {b}: {count_primes_in_range(a, b)}")
