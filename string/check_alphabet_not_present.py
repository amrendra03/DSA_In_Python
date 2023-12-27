# define a function to check for missing alphabets
def check_missing_alphabets(sentence):
    # create a set of all lowercase and uppercase alphabets
    lowercase_alphabets = set("abcdefghijklmnopqrstuvwxyz")
    uppercase_alphabets = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # convert the sentence to a set of lowercase letters
    sentence_letters = set(sentence.lower())

    # find the missing lowercase and uppercase letters
    missing_lowercase = lowercase_alphabets - sentence_letters
    missing_uppercase = uppercase_alphabets - set(sentence)

    # print the missing letters
    if len(missing_lowercase) > 0:
        print("The following lowercase letters are missing: " + ", ",sorted(missing_lowercase))
    if len(missing_uppercase) > 0:
        print("The following uppercase letters are missing: " + ", ",sorted(missing_uppercase))


# take user input for the sentence
sentence = input("Enter a sentence: ")

# call the function to check for missing alphabets
check_missing_alphabets(sentence)
