#print("Hello, World!")

'''
print("State your name:")
name = input()
print(f"hello, {name}")
'''


'''
i = 3
print(f"i is {i}")

f = 2.8
print(f"f is {f}")

b = True
print(f"b is {b}")

n = None
print(f"n is {n}")
'''


'''
x = 100

if x > 0:
    print("X is > 0")
elif x == 0:
    print("X == 0")
else:
    print("X is < 0")
'''


'''
name = "Alice"
coordinates = (10.0, 20.1)
names = ["Alice", "Bob", "Charlie"]

print(name)
print(coordinates)
print(names)

for name in names:
    print(name)
'''


'''
sets dont repeat
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2)
print(s)
'''

'''
#dictionary = {keys:value}

ages = {"Alice":20, "Bob":64}
ages["Sean"] = 30
ages["Sean"] += 1
print(ages["Alice"])
print(ages)
'''


def factorial(n):
    if(n <= 1):
        return 1
    return n * factorial(n - 1)

def main():
    print("hello")

if __name__ == "__main__":
    main()