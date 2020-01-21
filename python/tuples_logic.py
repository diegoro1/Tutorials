#----------------------------------------------------------------------------------------------------------
#                                             tuple + logic
#----------------------------------------------------------------------------------------------------------

# just like lists but CANNOT be changed (unless written over)
dimansions = (75,55)
random = [33, 45]
print(dimansions)

# this is a nono! dimansions[0] = 0
random[0] = 5
print(random)

# this is ok
dimansions = (0,55)
print(dimansions)

for i in range(0,11):
    if (i % 2) == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")

# even positive numbers
for i in range(-5,6):
    if ((i % 2) == 0) and (i > 0):
        print(str(i) + " is even and positive")
    elif (i % 2) == 0:
        print(str(i) + " is even and negative") 
    elif i > 0:
        print(str(i) + " is odd and positive")
    else:
        print(str(i) + " is odd and negative")

# if value is in a list
pizza = ['cheese', 'pepperoni', 'tomato', 'basil']
if 'cheese' in pizza:
    print("tango tango, we thriving")

if ('juice' in pizza) or ('tomato' in pizza):
    print('that was close!')

if 'apple' in pizza:
    print("what the hell is wrong with you?")

if 'apple' not in pizza:
    print("thank god.")

IamBetterThanYou = True
IamJoking = False #:)

# cheacking for an empty list
array = [0,1,2,3,4]
if array:
    print("list is not empty")
else:
    print("empty")

l = len(array)
for i in range(0,l):
    print(array.pop())
print(array)

if array:
    print("list is not empty")
else:
    print("empty")
