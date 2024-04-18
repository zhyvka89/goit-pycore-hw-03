import random


def get_numbers_ticket(min, max, quantity):
  try:
    if (min > 0 and max < 1000):
      range_of_numbers = range(min, max)
      random_numbers = random.sample(range_of_numbers, k=quantity)
      random_numbers.sort()
      return random_numbers
    else:
      return []
  except:
    print('Quantity must be smaller than max number')  

result = get_numbers_ticket(0, 999, 998)
print(result)