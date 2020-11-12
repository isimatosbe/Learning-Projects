print('\nWant to play with n-based numbers?')

while True:
    number = input('\nWhat\'s the number you want to convert? ')

    notCero1 = True
    while notCero1:
        base_number = input('\nIn which base is it? (Click enter if it\'s decimal) ')
        if base_number == '0':
            print('0 is not a valid base, choose another one please.')
        else:
            notCero1 = False
        
    if base_number == '':
        base_number = '10'

    notCero2 = True
    while notCero2:
        base_to = input('\nIn which base do you want to represent it? (Click enter if you want binary) ')
        if base_to == '0':
            print('0 is not a valid base, choose another one please.')
        else:
            notCero2 = False    
    
    if base_to == '':
        base_to = '2'
    base_to = int(base_to)

    len_number = len(number)
    base10_number = 0
    for i in range(0,len_number):
        base = int(base_number)
        base10_number = base10_number + int(number[i])*base**(len_number-1-i)

    nbase_number = ""
    if base_to == 1:
        for i in range(0,base10_number):
            nbase_number = '1' + nbase_number
    else:
        while base10_number > 0:
            remainder = base10_number % base_to
            base10_number = base10_number // base_to
            nbase_number = str(remainder) + nbase_number
    
    print(f"The number {number} in base {base_number} is {nbase_number} in base {base_to}.")

    play_again = input('Want to try another one? ')
    if play_again.lower() != 'yes':
        break