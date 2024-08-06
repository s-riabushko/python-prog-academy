import re

# Task 1
text = input('Enter a string: ')
pattern = 'Rb+r'
res = re.findall(pattern, text)
print(res)


# Task 2
card_number = input('Enter a card number: ')
pattern = r'(\d{4}-){3}\d{4}'
res = re.fullmatch(pattern, card_number)

if res:
    print(f"Card number '{card_number}' is valid")
else:
    print(f"Card number '{card_number}' is invalid")


# Task 3
email = input('Enter a email address: ')
pattern = r"^[A-Za-z0-9]+-{0,1}[A-Za-z0-9_]+@(\w+\.)+\w+"
res = re.fullmatch(pattern, email)

if res:
    print(f"Email '{email}' is valid")
else:
    print(f"Email '{email}' is invalid")


# Task 4
login = input('Enter a login: ')
pattern = "[a-zA-Z0-9]{2,8}"
res = re.fullmatch(pattern, login)

if res:
    print(f"Login '{login}' is valid")
else:
    print(f"Login '{login}' is invalid")

