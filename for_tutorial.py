# Example 1
# 'else' after for loop - executes after the for loop finishes (if not exited by 'break' !)
for n in range(2,10):
    for x in range (2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

