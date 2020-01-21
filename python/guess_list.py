#----------------------------------------------------------------------------------------------------------
#                                             Short List Exesise
#----------------------------------------------------------------------------------------------------------

guests = ['Joe','Jan','June','Julian','Jaylin','Jared']
print("invitations going to:")
for guest in guests:
    print("  ->" + guest)
print()

print("Oh no looks like " + guests.pop(1) + " won't make it")
guests.insert(1, 'John')
print("A new inviation to " + guests[1] + " will be sent!\n")

print("new list:")
for guest in guests:
    print("  ->" + guest)
print()

print("table got bigger, inserting someone in the start, middle, and end.\n")
guests.insert(0,'Jack')
guests.append('Jannet')
middle_index = int((len(guests) / 2))
guests.insert(middle_index, 'Jone')

print("new list:")
for guest in guests:
    print("  ->" + guest)
print()

print("invitations: ")
for guest in guests:
    print("Dear, " + guest + "\ncome eat yo.\nlove, me\n\n")

print("the dinner table broke! only two seats left!")
number_guests = len(guests)

while number_guests > 2:
    print("Sorry " + guests.pop() + " you are not invited! :)")
    number_guests = number_guests - 1

print()

print("invitations: ")
for guest in guests:
    print("Dear, " + guest + "\ncome eat yo.\nlove, me\n\n")

print("turns our " + guests[0] + " and " + guests[1] + " are not really your friends")
del guests[1]
del guests[0]

print("A list of who you're eating with: " + str(guests) + ".")

