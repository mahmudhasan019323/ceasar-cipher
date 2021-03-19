letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo = '''

 ██████╗███████╗ █████╗ ███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     █████╗  ███████║███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══╝  ██╔══██║╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗███████╗██║  ██║███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                               
'''

def ceasar_cipher():
    # print('\033c')
    print(logo, '\n')

    mode = int(input('Press 1 to encode and 2 to decode: '))
    text = input('enter you message : ')
    shift = int(input("type shift number : ") or 1) 

    if shift > len(letters):
        print('\033c')
        print(f'shift must be between 1 to {len(letters)}')
        ceasar_cipher()

    words = text.split(' ')
    new_words = []
    for word in words:
        new_word = ''
        if word == ' ':
            new_words.append(word)
            continue
        if mode == 1:
            for letter in word:
                if letters.index(letter) + shift + 1 > len(letters):
                    new_word += letters[shift - (len(letters) - letters.index(letter))]
                else:
                    new_word += letters[letters.index(letter) + shift]
        elif mode == 2:
            for letter in word:
                new_word += letters[letters.index(letter) - shift]
        new_words.append(new_word)
    print('your encoded message is : ' if mode == 1 else 'your decoded message is',' '.join(new_words))

    repeat = input("Do you want to exit. Type 'y' to exit. Default is 'n' : ").lower()
    if repeat == 'y':
        exit()
    else:
        print('\033c')
        ceasar_cipher()




ceasar_cipher()