def is_valid_sentence(sentence):

  # Adding exception handling to the code
  try:

      # Rule 1: String starts with a capital letter
      if not sentence[0].isupper():
        return False
  
       # Rule 2: String has an even number of quotation marks
      if sentence.count('"') % 2 != 0:
        return False
  
      # Rule 3: String end with a sentence termination character
      if sentence[-1] not in [".", "?", "!"]:
        return False
  
      # Rule 4: String has no period character other than the last character
      if sentence.count('.') > 1:
        return False
  
      # Split the sentence into words to check for numbers below 13
      words = sentence.split()
      for word in words:

        # Rule 5: Numbers below thirteen are spelled out
        if word.isdigit() and int(word) < 13:
          return False
    
      return True
  
  except IndexError:
    return False
  except ValueError:
    return False
  
# Get user input for the sentence
user_sentence = input("Enter a sentence: ")

# Check if the user has entered a valid sentence
result = is_valid_sentence(user_sentence)
if result:
  print("The entered sentence is valid.")
else: 
  print("The entered sentence is invalid.")




