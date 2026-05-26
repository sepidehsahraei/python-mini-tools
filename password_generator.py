import string
import random
def generate_password(length, include_special_characters=True):
    if include_special_characters:
        characters=string.ascii_letters + string.digits+string.punctuation
    else:
        characters=string.ascii_letters + string.digits
    password= ''
    for i in range(length):
        password+=random.choice(characters)
    return password

length=int(input ("Enter the length of the password: "))
answer=input("Do you want to include special characters? (yes/no): ")
while answer.lower() not in ['yes', 'no']:
    print("Invalid input. Please enter 'yes' or 'no'.")
    answer=input("Do you want to include special characters? (yes/no): ")
print('Generated Password:', generate_password(length, include_special_characters=(answer.lower()=='yes')))
