i = 1


def is_prime(n):
    global i
    i = i + 1
    if (n < 2):
        return False
    if (i == n):
        return True
    if (n % i == 0):
        return False
    return is_prime(n)
