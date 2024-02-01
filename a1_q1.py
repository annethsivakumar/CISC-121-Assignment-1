"""
CISC-121 2023W
Name: Anneth Sivakumar
Student Number: 20320973
Email: 21as221@queensu.ca
Date: 2023-01-18
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
import random

def calculate_difference(number_1, number_2):
  """
  This function returns the difference between two numbers once it determines it is a valid number.
  Parameters: number_1 - integer of one of the randomized chosen numbers.
              number_2 - integer of another randomized chosen numbers.
  Return: large_number - integer of the larger number of the two chosen number.
          small_number - integer of the smaller number of the two chosen number.
  """
  # Determine larger number and smaller number.
  large_number = max(number_1, number_2)
  small_number = min(number_1, number_2)
  # Determine the difference of the two number
  difference = large_number - small_number
  # If difference is not between 10 and 50 - state that this pair of integers is invalid.
  while (difference < 10 or difference > 50):
    print("Two randomly generated integer numbers are " + str(small_number) +
          " and " + str(large_number))
    print("This pair of integers is invalid.")
    # If the pair is too close together, replace the larger number with two times that number.
    if (difference < 10):
      large_number = large_number * 2
    # If the pair is too far apart, replace the larger number with a third of that number rounded up.
    if (difference > 50):
      large_number = int(large_number / 3)
    # Determine the difference of new numbers.
    difference = large_number - small_number
  # State that the pair of integers is valid.
  print("Two randomly generated integer numbers are " + str(small_number) +
        " and " + str(large_number))
  print("This pair of integers is valid.")
  return large_number, small_number


def replace_numbers(large_number, small_number):
  """
  This function is used replace and print specific numbers with specific text, if conditions are True.
  Parameters: large_number - integer of the larger number of the two numbers.
              small_number - integer of the smaller number of the two numbers.
  Return: None.
  """
  print("\n" + "Output for the valid numbers " + str(small_number) + "," +
        str(large_number) + ":")
  # Go through each number from small to large.
  for num in range(small_number, large_number + 1):
    # sub_word variable is an empty string for storing words.
    sub_word = ""
    # If number is a multiple of five, add apple.
    if (num % 5 == 0 and num != 0):
      sub_word += "apple "
    # If number is a multiple of seven, add pen.
    if (num % 7 == 0 and num != 0):
      sub_word += "pen "
    # If number contains three, add pineapple.
    if ("3" in str(num)):
      sub_word += "pineapple "
    # Check if sub_word is an empty string, else print number.
    if sub_word:
      print(sub_word)
    else:
      print(num)


def main():
  """
  This function implements the interface for the program.
  Parameters: None.
  Return: None.
  """
  # Generate two random numbers from 0 to 100.
  number_1 = random.randint(0, 100)
  number_2 = random.randint(0, 100)
  # Call calculate_difference to receive larger number, smaller number.
  difference = calculate_difference(number_1, number_2)
  # Call replace_numbers to print all the numbers with text replacements.
  # difference[0] - represents larger number.
  # difference[1] - represents smaller number.
  replace_numbers(difference[0], difference[1])


main()