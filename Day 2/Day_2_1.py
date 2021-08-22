#Who's paying
import random

test_seed =int(input("Create a seed Number: "))
random.seed(test_seed)

name = input("Enter ur Name seperated by a Comma. ")
namelist = name.split(",")

print(namelist)

length = len(namelist)
lenght2 = random.randint(0,length-1)


print(f"{namelist[lenght2]} will pay the bill")
