# This code checks if the password is secure. Secure password is:
# 8 or more symbols
# At least 1 upper case symbol
# At least 1 lower case symbol
# At least 1 digit.

# объявление функции
def is_password_good(password):
    counter = 0
    if password.islower() == False:
        counter += 1
    if password.isupper() == False:
        counter += 1
    for i in password:
        if i in '1234567890':
            counter += 1
            break
    if len(password) >= 8:
        counter += 1
    if counter == 4:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))