letter = input("Enter a letter and we'll tell you if it's a vowel: ")

if len(letter) == 1: 
    if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' \
    or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
        print(f"the {letter} is a vowel") 
    else:
        print(f"the {letter} isn't a vowel") 
else:
    print(f"Can't process the requested letter {letter}.")
    