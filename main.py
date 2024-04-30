import random
import time

print("Welcome to the password generator. It will create the most sadest passwords of all time.")
print("Please wait your password is getting ready")

# n = input("")

l1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

l2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

l3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] 


l4 = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}"]

# Start of taking random alphabets
for alpha1 in range(1):
    r = random.choice(l1)
    r2 = random.choice(l2)
    r3 = random.choice(l1)
    r4 = random.choice(l2)
    r5 = random.choice(l1)
    r6 = random.choice(l2)
# Start of taking random numeric.
for num in range(1):
    r7 = random.choice(l3)
    r8 = random.choice(l3)
    r9 = random.choice(l3)
# Start of taking random special charecters
for spc in range(1):
    r10 = random.choice(l4)
    r11 = random.choice(l4)
    r12 = random.choice(l4)
time.sleep(2.5)
print(r+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12, "Your password is ready", end="")




