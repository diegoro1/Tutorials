#----------------------------------------------------------------------------------------------------------
#                                             Srtrings
#----------------------------------------------------------------------------------------------------------

messege = "hello python!"
print(messege)

# strings
messege = "this is normal"
funcky_message = 'this is also ok!'
print(messege)
print(funcky_message)

# a nice way to make a title
print(funcky_message.title())

# lets have some fun
print("lets make is upper case!: " + funcky_message.upper())
print("Now lower!!: " + funcky_message.lower())
print("normal state: " + funcky_message)
funcky_message = funcky_message.upper()
print(funcky_message)
funcky_message.lower() #this wont change anything! see why? :)
print(funcky_message)

# all of this should look familiar, including this!
print("\nI\nneed\nsome\n\t\tSPACE")
print("I love:\n\t*lists\n\t*organaized lists\n\t*ugly formatting")

# eliminating whitespace / space
peace = "a lot"
print(peace)
nightmare = peace.replace(' ', '')
print(nightmare)
right_space = ' opps'
print(right_space)
nospace = right_space.lstrip()
print(nospace)

# invlaid syntax with ' and "
# "you're ok here!"
# 'you're screwed' :)


