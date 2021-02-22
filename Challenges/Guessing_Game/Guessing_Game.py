print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER\n")

from random import randint
correct_number = randint(1,100)

# list to save guesses
my_guesses = []

while True:
  pick_a_number = int(input('Please guess a number between 1 and 100: '))
  if pick_a_number < 1 or pick_a_number > 100:
    print('Error, your number is not between 1 and 100')
    # Back to the beginning of the loop
    continue
  
  # Add guess to the list
  my_guesses.append(pick_a_number)
  
  # First guess and corrent
  if pick_a_number == correct_number and len(my_guesses) == 1:
    print(f'Congratulation, you guessed it in only {len(my_guesses)} guess')
    break
  # Correct but more than 1 guesses
  elif pick_a_number == correct_number:
    print(f'\nCongratulation, you guessed it in {len(my_guesses)} guesses')
    break
  
  # First guess but not correct
  if len(my_guesses) == 1:
    # Jika abs(Nilai Benar - First Guess) dengan selisih kurang dari / sama dengan 10 maka WARM (Dekat dengan Nilai Benar)
    if abs(correct_number - my_guesses[0]) <= 10:
      print('WARM')
    # Sebaliknya
    else:
      print('COLD')
  # More than 1 guess
  else:
    # Jika abs(Nilai Benar - Current Guess) lebih kecil dari abs(Nilai Benar - Previous Guess) maka WARMER (Mendekati Nilai Benar)
    if abs(correct_number - my_guesses[-1]) < abs(correct_number - my_guesses[-2]):
      print('WARMER')
    # Sebaliknya
    else:
      print('COLDER')
