import random


def word_guess():
    words_repository = ['hang', 'dare', 'truth', 'sky', 'peace', 'hello']
    comp_choose = random.choice(words_repository)
    # comp_choose is converted to list to use  'pop' and 'insert' methods. 
    comp_choose_list = [letter for letter in comp_choose]
    # comp_choose_length will be used as a hint to the user.
    comp_choose_length = len(comp_choose)  
    current_attempt = correct_attempt = wrong_attempt = 0
    max_attempts = 7
    print(f'This is the Word guess game. You have only {max_attempts} guesses in total. Best of luck.')
    # Taking the input from the user.
    while current_attempt < max_attempts:
        # Break the while loop, if correct word is guessed before maximum attempts gets exhausted.
        if correct_attempt == comp_choose_length:
            break

        # If user wants to guess the complete word instead of letters.
        if correct_attempt >= max_attempts // 2:
            print(
                'Do you want to guess the word instead of letters? Press "1" for yes and "0" for continuing with letters instead.')
            try:
                yes_or_no = int(input())
                if yes_or_no == 1:
                    user_guess_word = input('Enter the word:').lower()
                    current_attempt += 1
                    if user_guess_word == comp_choose:
                        print(f'You guessed the correct word in {current_attempt} attempt.')
                    else:
                        print(f'Wrong guess. {max_attempts - current_attempt} attempt remaining.\nTry again')
                        wrong_attempt += 1
                        continue
                elif yes_or_no == 0:
                    pass
                else:
                    print('Invalid input. Try again!')
                    continue
            except Exception:
                print('Invalid input! Try again')
                continue

        # If user wants to guess the word using the letters only.
        user_guess_letter = input('Enter the letter:').lower()
        if not user_guess_letter.isalpha():
            print('Invalid input!!\nPlease enter letter only!')
            continue
        current_attempt += 1

        # Check if the user's guessed letter is available in comp_choose_list.
        if user_guess_letter in comp_choose_list:
            letter_index = comp_choose_list.index(user_guess_letter)
            print(
                f'You guessed the correct letter.Letter position is {letter_index + 1} in the word.\n\t{max_attempts - current_attempt} guess remaining!')
            # Pop and insert is used for multiple occurrences of letter.
            comp_choose_list.pop(letter_index)
            comp_choose_list.insert(letter_index, '_')
            correct_attempt += 1
        else:
            print(f'Wrong guess! {max_attempts - current_attempt} guess remaining!\nTry again.')
            wrong_attempt += 1
        # Hint for the user if he gave two or more wrong attempts.
        if wrong_attempt == 2:
            print(f'\tHint for you. (Word has {comp_choose_length} letters.)')
        elif correct_attempt == 0 and wrong_attempt > max_attempts // 2:
            print(
                f'Smart Hint -> (Word starts with {comp_choose[0]} and ends with {comp_choose[comp_choose_length - 1]})')
    # After the exhaustion of the while loop,we check for the final result.
    if correct_attempt == comp_choose_length:
        print(f'You guessed the correct word {comp_choose} in {current_attempt} attempt.')
    else:
        print('You failed to guess the correct word!!\n\t If you want to play again press "1" or press "0" to quit.')
        while True:
            try:
                play_again = int(input())
                if play_again == 1:
                    word_guess()
                elif play_again == 0:
                    print('Game Ended.')
                    break
                else:
                    print('Invalid input! Try again')
            except Exception:
                print('Invalid input! Try again.')


word_guess()
