def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    price1 = float(input('Price of item one? '))
    price2 = float(input('Price of item two '))
    price3 = float(input('Price of item three? '))
    price4 = float(input('Price of item four? '))
    price5 = float(input('Price of item five? '))

    subtotal = round(price1 + price2 + price3 + price4 + price5, 2)
    salesTax = round(subtotal * 0.07, 2)
    total = subtotal + salesTax

    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Sales Tax: ${salesTax:.2f}')
    print(f'Total: ${total:.2f}')


calculate_total_purchase()