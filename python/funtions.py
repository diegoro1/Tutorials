def multiply(a, b):
    return a * b

def multiplier(a, b=1):
    return a * b

def print_name(fname, lname, midname=''):
    if midname:
        name = fname + " " + midname + " " + lname 
        print(name.title())
    else:
        name = f"{fname} {lname}"
        print(name.title())

print(multiply(2,3))
print(multiplier(20))
print_name("oto", "herrason", 'goop')
print_name("oto", "popo")


