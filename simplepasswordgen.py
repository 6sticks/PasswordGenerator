import random as rng
import time
import sys
randomNumbers = rng.choice([1,2,3,4,5,6,7,8,9,10]) + rng.choice([1,2,3,4,5,6,7,8,9,10])+ rng.choice([1,2,3,4,5,6,7,8,9,10])+ rng.choice([1,2,3,4,5,6,7,8,9,10])+ rng.choice([1,2,3,4,5,6,7,8,9,10])+ rng.choice([1,2,3,4,5,6,7,8,9,10])+ rng.choice([1,2,3,4,5,6,7,8,9,10])+ rng.choice([1,2,3,4,5,6,7,8,9,10])
randomWords = ["drake", "garden", "pokemon", "juice", "worker", "robot", "artifact", "food", "follower", "confident", "messy", "sandwich", "farmer"]
print("Time to make a super secure password")
firstName = input("What is your first name? : ")
lastInitial = input("What is the initial of your last name? : ")
addedWord = rng.choice(randomWords)
collectedData = firstName + lastInitial + addedWord + str(randomNumbers)
listedValues = [firstName, lastInitial, addedWord, str(randomNumbers)]
spaceCheck = (" " in firstName) or (" " in lastInitial)
if spaceCheck == True:
    print("No spaces in first name or last initial answer")
    input("Press ENTER to exit and try again")
    sys.exit()
else:
    rng.shuffle(listedValues)
realPass = ''.join(listedValues)
x = 1
y = 1
z = 75
while y <= z:
    y = x + y
    print("Generating password...")
    time.sleep(.0025)

if y >= z:
    print(" ")
    print(realPass)
    print(" ")
    input("Press ENTER to exit")
