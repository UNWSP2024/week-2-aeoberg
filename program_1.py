def personal_information():
    name = input('What is your name?')
    address = input('What is your address - with city, state, and zip?')
    phone_number = input('What is your phone number?')
    major = input('What is your college major?')

    print()
    print(name)
    print(address)
    print(phone_number)
    print(major)


# Line which calls the above function.
personal_information()