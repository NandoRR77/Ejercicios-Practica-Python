'''
def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE

    tax = round(((subtotal * 15) / 100),2)
    
    return float(tax)

tax = calculate_tax(1000000)
print("Tax for the order is: " + str(tax))
'''

order = [{'name': 'espresso', 'price': 1.99}, {'name': 'coffee', 'price': 2.5}, {'name': 'cake', 'price': 2.79}]

'''
def calculate_subtotal(order):
    subtotal = 0
        
    for i in order:
        subtotal += i['price']
    return float(subtotal)
'''


def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names - OK
        3. Return names and total. - OK

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total

    """
    #print_order(order)
    ### WRITE SOLUTION HERE
    total = 0 
    
    names = []
    
    for i in order:
        names.append(i['name'])
        total += i['price']
        
    total += ((total * 15) / 100)
    total = float(round((total),2))
    
    return names, total

    raise NotImplementedError()

print(summarize_order(order))

#print(calculate_subtotal(order))
