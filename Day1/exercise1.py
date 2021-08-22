  
# heads and tails Exercise

import random

test_seed = int(input("Create a seed Number: "))
random.seed(test_seed)
random_int = random.randint(0,1)
if random_int ==0:
  print("heads")
else:
  print("tails")
