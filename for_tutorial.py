# Example 1
# 'else' after for loop - executes after the for loop finishes (if not exited by 'break' !)
for n in range(2,10):
    for x in range (2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


# Example 2
# 'continue' go to next iteration of the loop
for n in range(2,10):
    if n % 2 == 0:
        print(n, 'is even number')
        continue
    print(n, 'is odd number')

# Example 3
# Using copy of a list while iterating over it by slice [:]
# Without the copy it would be infinite loop
mylist = ['this', 'is', 'cool', 'construction']
for item in mylist[:]:
    if len(item)>5:
        mylist.insert(0, item)
print(mylist)
