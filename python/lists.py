#----------------------------------------------------------------------------------------------------------
#                                             Lists
#----------------------------------------------------------------------------------------------------------
from random import randint
from random import seed

planets = ['mercury', 'venus', 'earth', 'mars']
print(planets)

# they kid of work like arrays at first glance
print(planets[0])

for planet in planets:  # this should give you ptsd! :)
    print(planet)
print("")

#now this is BEzarre
print(planets[-1]) # it went the other way!
print("")

# lists are dynamic, i like to think of them as a linked list. 
# (this can be a completly ignorant way of thinking)
planets.append('jupter')

for planet in planets:
    print(planet)
print()

# this is pure convenience
planets.insert(0, 'sun')
for planet in planets:
    print(planet)
print()

# this is very ugly but useful
del planets[0]
for planet in planets:
    print(planet)
print()

#pop() (guess i wasnt so ignorant)
popped = planets.pop()
print('popped: ' + popped + '\n')
for planet in planets:
    print(planet)
print()

# is this a god like data structure or just linked list with very nice methods pre implemented?
planets.append('jupiter')
for planet in planets:
    print(planet)
print()

popped = planets.pop(1)
print('popped: ' + popped + '\n')
for planet in planets:
    print(planet)
print()

planets.insert(1, 'venus')
for planet in planets:
    print(planet)
print()

# now this is gettung ridiculous! no onde why everyone ditch good boy C
planets.remove('mars')
planets.insert(3, 'ellon musk retreat')
for planet in planets:
    print(planet)
print()

#sorting
# .sort is O(nlogn) (need to see what type of sort, most likely quick sort)
array = []
seed(1)
for i in range(15):
    array.append(randint(0,101))
    print(array[i], end= " ")

print("\nsorting:----------")

array.sort()
for i in array:
    print(i, end=" ")

print("\nreversing:----------") #this is nice!

array.sort(reverse=True)
for i in array:
    print(i, end=" ")

print("\ntemporary sort")
print(sorted(array))
for i in array:
    print(i, end=" ")

print("\nthis also reverses")
array.reverse()
for i in array:
    print(i, end=" ")
print()

print("the len of array == " + str(len(array)))

# random stuff
food = ['eggs', 'cheese', 'steak', 'lobster', 'olive', 'bread']
print(food)
print("by value")
print(sorted(food))
print("by value")
print(sorted(food, reverse=True))
print("proof")
print(food)
print("by reff")
food.sort()
print(food)
food.sort(reverse=True)
print(food)


# reflection: Lists seemed to be a doobled liked list, 
# due to the -1 index nature and being able to go around
# might be completly wrong though, but i like this data struct so far

