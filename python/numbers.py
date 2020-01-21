#----------------------------------------------------------------------------------------------------------
#                                             Numbers
#----------------------------------------------------------------------------------------------------------

from random import randint
from random import seed
seed(1)

float1 = 0.1
float2 = 0.2
print(float1 + float2) # what the hell happend here? hypot: binary.

# int to str convert
age = randint(1,101)
message = "hello! I am " + str(age) + " years old!"
print(message)
