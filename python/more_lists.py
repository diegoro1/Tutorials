#----------------------------------------------------------------------------------------------------------
#                                             Numbers
#----------------------------------------------------------------------------------------------------------

# printing even nymbers using range
for i in range(0,11,2): # 0 is even you nerds.
    print(i, end=" ")
    if i == 10:
        print()

# printing odd numbers
for i in range(1,11,2):
    print(i, end=" ")
    if i == 9:
        print()

# factorial (i completly wung this *pats back* now i know how to create funtions!)
def factorial(i):
    if i < 2:
        return 1
    i = i * factorial(i - 1)
    return i

print(factorial(5))

# i^2
squares = []
for i in range(0,10):
    squares.append(i * i)
    print(squares[i], end=" ")
print()

print(max(squares))
print(min(squares))
print(sum(squares)) # sum of all elements

# i find this one liner compeletly horrid
ugly = [i**2 for i in range(0,11)]
print(ugly)

uglry = [i**3 for i in range(0,11)]
print(uglry)

# slicing
prime = [2,3,5,7,11,13,17]
print(prime[0:4])
print(prime[:4]) # see how this is the same?
print(prime[4:])

# our bizarre frind is back
print(prime[-3:]) # see how this is th same as above?

# slicing for loops
for i in prime[:4]:
    print(i, end=" ")
print()

# copying lists
animals = ['cow', 'dog']
mammals = animals[:]

# this is WRONG!
# mammals = animals
# we are making mammals POINT to animals!!!!! BAD (in this case at least)

animals.append('goldfish')
mammals.append('dolphin')

print(animals)
print(mammals)
