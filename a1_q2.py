import random

def add_data():
  """
  This function appends user's and one other person's data to myspace_profiles.txt.
  Parameters: None.
  Returns: None.
  """
  # Open file for appending
  myspace_data = open("myspace_profiles.txt", "a")
  # Ask user for their name, age and color.
  user_name = input("Enter your name: ")
  user_age = input("Enter your age: ")
  user_color = input("Enter your favorite color: ")
  # Append user's data to the end of the file.
  myspace_data.write(user_name + "\n" + user_age + "\n" + user_color + "\n")
  # Ask user for name.
  person_name = input("\n" + "Enter another person's name: ")
  # Generate random age for person.
  random_age = random.randint(18, 22)
  # Choose random favorite color for person.
  colors = ["green", "red", "yellow", "pink", "blue", "orange"]
  random_color = random.choice(colors)
  # Append person's data to the end of the myspace_profiles.txt file.
  myspace_data.write("-" + "\n" + person_name + "\n" + str(random_age) + "\n" +
               random_color + "\n")
  # Enter dash to close off data for last person.
  myspace_data.write("-" + "\n")
  myspace_data.close


def print_data():
  """
  This function prints the contents of myspace_profiles.txt.
  Parameters: None.
  Returns: None.
  """
  # Open file for reading.
  myspace_data = open("myspace_profiles.txt", "r")
  # Store contents in a variable, close file, and print data.
  file_contents = myspace_data.read()
  myspace_data.close()
  print(file_contents)


def main():
  """
  This function implements the user interface for the program.
  Parameters: None.
  Return: None.
  """
  # Call add_data to add new data to .txt file.
  add_data()
  # Call print_data to print the .txt file with new content.
  print_data()


main()
