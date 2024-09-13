def average_age():
    # Get User Input
    age1 = int(input('How old is friend one? '))
    age2 = int(input('How old is friend two? '))
    age3 = int(input('How old is friend three? '))
    age4 = int(input('How old is friend four? '))
    age5 = int(input('How old is friend five? '))
    # Sum ages
    sum = age1 + age2 + age3 + age4 + age5
    # Average the ages
    average = sum / 5

    # Print the results
    print(average)

# Line which calls the above function.
average_age()