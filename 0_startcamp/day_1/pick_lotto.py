import random

numbers = list(range(1,46))

pick = random.sample(numbers,6)

print(sorted(pick))

# print(random.sample(list(range(1,46)),6))