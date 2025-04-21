def computer_guesses_number():
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("After each guess, tell me if it's:")
    print("'h' if my guess is too high, 'l' if it's too low, or 'c' if it's correct.")

    low = 1
    high = 100
    guesses = 0

    while True:
        if low > high:
            print("Hmm... something went wrong. Did you give honest hints? 😅")
            break

        guess = (low + high) // 2
        guesses += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 Yay! I guessed your number in {guesses} tries!")
            break
        else:
            print("Please enter 'h', 'l', or 'c'.")

# Start the game
computer_guesses_number()
