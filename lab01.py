import random
attempts = 0
guesses = []
number = -1

print('This is the "guess a number" game.')
print("You try to guess a random number in the smallest number of attempts.")
range = int(input("\nPick a positive integer: "))
print(f"Guess a number between 1 and {range}.")


secret_number = random.randint(1,range)


while secret_number != number:
    number = int(input("> "))
    guesses.append(number)
    if number < secret_number:
        print("     Too low!")
    elif number > secret_number:
        print("     Too high!")
    attempts += 1

print(f"You were able to find the number in {attempts} guesses.")
print(f"The numbers you guessed were: {guesses}")

# 1. Name:
#      Brock Hoskins
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      This program generates a random number between 1 and a given range from the user and the user guesses what the random number is.
# 4. What was the hardest part? Be as specific as possible.
#      The only difficulty I had was converting the user's input into an integer. I realized that I can't type int(input), but instead int(input()).
# 5. How long did it take for you to complete the assignment?
#      It probably took a little under an hour to complete the assgnment.