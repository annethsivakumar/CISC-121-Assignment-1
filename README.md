Question 1
---------------
Write a program that randomly generates two integers between 0 and 100. You should then
check if the difference between these two numbers is at least 10 and no more than 50 and
accordingly print a statement saying “This pair of integers is valid” or “This pair of integers is
invalid.” Whenever the pair is too close together, replace the larger number with two times that
number. Whenever the pair is too far apart, replace the larger number with a third of that
number rounded UP (not down). Repeat the process until both numbers are valid.
Once these numbers are valid proceed as per the following:

- Print each of the numbers from the smallest (first number) to the largest (second
number). Instead of printing the number do the following whenever the specified
conditions are satisfied.
  - Print apple whenever the number is a multiple of 5
  - Print pen whenever the number is a multiple of 7
  - Whenever the number contains a 3 print pineapple

- These conditions should stack. So the number 35 should print apple pen pineapple
in the same line.

Sample run:
Two randomly generated integer numbers are 0 and 12
This pair of integers is valid
Output for the valid numbers 0,12:
  - 0
  - 1
  - 2
  - pineapple
  - 4
  - apple
  - 6
  - pen
  - 8
  - 9
  - apple
  - 11
  - 12


Question 2
--------------
The text file myspace_profiles.txt contains information about some people. For each person in
the file it has their name, their age, and their favorite color each on a new line. Each person is
separated by a ‘-’ on its own line.
Write a program that adds yourself to the given file at the end of the file, without damaging the
previous data. After that, add another person to the file by:
- taking the name from the user input
- their age should be between 18-22 (randomly generated)
- their favorite color is one of ‘green, red, yellow, pink, blue, orange’ (randomly generated)

Once you are finished writing to the file, display the contents of the file
