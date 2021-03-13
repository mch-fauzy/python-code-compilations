"""
Write a `function` that returns the `*number* of prime numbers` that `exist up to` and `including a given number`

    count_primes(100) --> 25

By convention, 0 and 1 are not prime.

In math, prime numbers are whole numbers greater than 1, that have only two factors – 1 and the number itself.

`Prime numbers` are `divisible` only by the number 1 or itself.
"""

def count_primes(num):
  # Counter
  count = 0

  # List of Primes Number
  primes = []

  # Looping Angka yang akan dibagi
  for number in range(num + 1):
    # Jika number kurang dari 2, go to the next number (0 dan 1 bukan bil. prima)
    if number <= 1:
      continue

    # Looping Pembagi
    for pembagi in range(2, number):
      
      # Uji Prime Number
      # Bil. Prima adalah suatu angka jika dibagi dengan angka SELAIN 1 DAN angka-itu sendiri BERSISA 0
      # 9 % 3 = 0 (sisa 0) maka bukan bil. prima
      if (number % pembagi) == 0:
        break

    # If loops end (not break or continue), go to this statement
    else:
      primes.append(number)
      count += 1

  print(primes)
  return count

# Check
print(count_primes(25))