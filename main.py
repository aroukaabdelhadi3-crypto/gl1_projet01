import random 
import string 

lettrs = string.ascii_letters 
c = ""
while c!= "w":
    c=random.choice(lettrs)
    print (f"la lettre choisir est {c}")

