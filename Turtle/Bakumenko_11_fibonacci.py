def fibonacci_member(n):
    if n <= 2:
        return n
    else:
        return fibonacci_member(n-2)+fibonacci_member(n-1)


a = int(input())
print(fibonacci_member(a))