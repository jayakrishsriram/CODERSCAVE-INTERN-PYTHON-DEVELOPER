import string
import random
def password_gen(m=3):
    l=string.ascii_letters + string.digits+ string.punctuation
    password=" ".join(random.choice(l) for i in range(m))
    print(password)
try:
    password_gen(int(input("Enter the length of the password:")))
except:
    password_gen()