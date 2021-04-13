import random

rand=(random.randint(1, 9))
introString =int(input("guess a number between( 1-9)"))
print(introString)
if(introString==rand):
        input("you have guessed it right")


if(introString>rand):
     input("you have guessedit wrong   HINT:try lower numbers")

if(introString<rand):
     input("you have guessedit wrong HINT:try higher numbers")       