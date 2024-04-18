import re

def normalize_phone(phone_number):
  pattern = r"[^+\d]"
  modified_number = re.sub(pattern, "", phone_number)
  country_code = "+38"
  if (modified_number.startswith(country_code)):
    return modified_number
  elif (modified_number.startswith("380")):
    return "+" + modified_number
  else:
    return country_code + modified_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)