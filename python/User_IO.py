"""
messege = input("Quack Quack! I am a parrot!... ")
print(messege + " ...quack!!!")

name = input("Enter Name: ")
print(f"Your name is: {name}")

age = input("Enter Age: ")
age = int(age)

if age >= 18:
    print("Congratulations! you're going to war!!")
else:
    print("Lucky Bastard!")

i = 5
while i < 8:
    print(f"This is annoying {i}", end="")
    print() if (i == 7) else print(end=" ")
    i = i + 1

print("please enter a word to get it all caps! ('quit' to end):")
word = input()
while word != 'quit':
    print(word.upper())
    print("please enter a word to get it all caps! ('quit' to end):")
    word = input()


print("pick a integer from 1 - 10 (0 to quit)")
number = int(input())
while True:
    if number == 0:
        print("thats right!")
        break
    elif number > 7:
        print("too high")
    else:
        print("too low")
    print("try again")
    number = int(input())

topping = ['cheese', 'banana', 'steak']
print("Enter topping and we'll check if we got it! ('no' to quit)")
item = 'null'
while True:
    item = input("->")
    if item == 'no' or item == 'No' or item == 'NO':
        break
    if item not in topping:      
        print("not a topping.")             
        continue 
    
    print(f"{item} is a topping!")

"""