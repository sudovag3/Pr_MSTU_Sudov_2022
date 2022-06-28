import random
# import generator.SolvingNonlinearEquations as snp

def generate_password(length, uppercase, numbers, special):
    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if numbers:
        characters.extend(list('1234567890'))
    if special:
        characters.extend(list('!@#$%^&*()!@#$%^&*()'))
    for x in range(length):
        password += random.choice(characters)


    return password



