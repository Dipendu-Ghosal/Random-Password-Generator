import random
import string

password_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation
# password = ""
# for i in range(password_len):
#     password += random.choice(charValues)
password = "".join([random.choice(charValues) for i in range (password_len)])

print(f"Your password is - {password}")