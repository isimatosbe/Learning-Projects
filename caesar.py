print("\nWant to play a little bit with Caesar Cipher? \nLet's go!")

# I am going to use chr() (from an int returns and ASCII character chr(65) == 'A')
# and ord() (from a character returns an int ord('A') == 65)

def caesar_cipher(message,offset):
    # Our message is going to be in capitals already
    len_mes = len(message)
    message_encrypted = ""
    for i in range(len_mes):
        letter = message[i]
        movement = (ord(letter) - 65 + offset) % 26
        message_encrypted = message_encrypted + chr (65 + movement)
    return message_encrypted

while True:
    option = int(input("\nDo you want to encrypt (press 1) or decrypt (press 2)? "))
    
    if option == 1:
        message = input("What message do you want to encrypt? ")
    else:
        message = input("What message do you want to decrypt? ")
    message = message.upper()
    message = message.split()

    offset = (-1)**(option + 1) * int(input("What offset do you want to use? "))

    message_encrypted = []
    for word in message:
        word_encrypted = caesar_cipher(word,offset)
        message_encrypted = message_encrypted + [word_encrypted]
    message_encrypted = ' '.join(message_encrypted)

    if option == 1:
        print(f"Your message encrypted is {message_encrypted}")
    else:
        print(f"Your message decrypted is {message_encrypted}")

    play_again = input('De you Want to encrypt/decrypt anything else? ')
    if not(play_again.lower() == 'yes'):
        break