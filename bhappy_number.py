print('\nLet\'s have some fun with b-Happy Numbers! \n')

def number_to_base(number,base):
    bbase_number = ""
    if base == 1:
        while len(bbase_number) < number:
            bbase_number = '1' + bbase_number
    else:
        while number > 0:
            remainder = number % base
            number = number // base
            bbase_number = str(remainder) + bbase_number
    return(bbase_number)

def is_happy(number,base):
    bucle = []
    our_number = number
    while our_number != 1 and not(our_number in bucle):
        # We put the number given (or the sum of the squares) 
        # in base b and repeat.
        bbase_number = number_to_base(our_number,base)

        sqrt_sum = 0
        for i in bbase_number:
            sqrt_sum = int(i)**2 + sqrt_sum
        bucle = bucle + [our_number]
        our_number = sqrt_sum

    if our_number == 1:
        print(f"Congratulations! {number} is {base}-happy.")
    else:
        print(f"Sorry, {number} is not {base}-happy.")
        print(bucle + [our_number])


while True:
    # We ask the user for a base 10 number.
    number = input("Which number do you want to know if is b-happy? ")
    number = int(number)

    # We ask for the base he wants to use, to check if is b-Happy
    # we should display a warning error if the base is 0.
    baseNotCero = True
    while baseNotCero:
        base = input("\nIn which base are we playing? ")
        base = int(base)
        if base == 0:
            print('0 is not a valid base, choose another one please.')
        else:
            baseNotCero = False
    
    is_happy(number,base)

    play_again = input('Want to try another one? ')
    if play_again.lower() != 'yes':
        break