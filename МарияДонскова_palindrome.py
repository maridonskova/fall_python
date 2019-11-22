
def palindrome(a):
    if len(a) < 2:
        return True
    if a[0] != a[-1]:
        return False
    return palindrome(a[1:-1])
