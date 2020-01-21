#----------------------------------------------------------------------------------------------------------
#                                             Short List Exesise
#----------------------------------------------------------------------------------------------------------


stundent0 = {'ID':'0022', 'GPA':3.2}
stundent1 = {'ID':'0023', 'GPA':3.78}

print(stundent0['ID'])
print(stundent1['GPA'])

fetch_data = stundent0['ID']
print("fetching data for " + str(fetch_data))

stundent0['standing'] = "freshman"
print(stundent0['standing'])

stundent0['standing'] = "junior"
print(stundent0['standing'])

stundent0['type'] = "bad"
stundent1['type'] = "good"

def GPAcalc(stundent):
    if stundent['type'] == "bad":
        stundent["GPA"] = stundent["GPA"] - 1
    else:
        stundent["GPA"] = stundent["GPA"] + 1

GPAcalc(stundent0)
GPAcalc(stundent0)

print(stundent0["GPA"])

del stundent0['standing']
print(stundent0)

fav_lang = {
    'bob': 'c',
    'tod': 'c#',
    'rob': 'java',
    'me': 'machine code cause im hardcore',
    'you': 'python',
    'us': 'python'
}

print("my fav lang is: " + fav_lang['me'])
print()

# looping through a dictionary
for key, value in stundent0.items():
    print("key: " + str(key))
    print("value: " + str(value))

if 'rud' not in fav_lang.keys():
    print("missing rud")

for name in fav_lang.keys():
    print(name)

for name in sorted(fav_lang.keys()):
    print(name)

print()
for v in fav_lang.values():
    print(v.title())

for value in set(fav_lang.values()):
    print(value)

# list of dictionaries
alien0 = {'color': 'green', 'points': 25}
alien1 = {'color': 'yellow', 'points': 15}
alien2 = {'color': 'blue', 'points': 35}
alien3 = {'color': 'red', 'points': 100}

aliens = [alien0,alien1,alien2, alien3]
for alien in aliens:
    print(alien)

# list in a dic
pizza = {
    'crust': 'thin',
    'toppings': ['chesse', 'ham'],
}

print("you ordered a " + pizza['crust'] + " pizza")
print("with toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

fav_langs = {
    'jan': ['ruby', 'pearl'],
    'john': ['javascript', 'php'],
    'june': ['python', 'r'],
    'me': ['c', 'c#'],
}

for key, value in fav_langs.items():
    print(key + ":", end=" ")
    for lang in value:
        print(lang, end=" ")
    print()

# dict of dict
user = {
    'fmerc': {
        'f_name':'fred',
        'l_name':'mercury',
    },
    'musky':{
        'f_name':'elon',
        'l_name':'musk',
    },
}

for uname, infos in user.items():
    print(uname, end=": ")
    for info in infos.values():
        print(info, end=" ")
    print()
