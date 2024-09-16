import os
import re
import string

# Ask the user to input a specific filename in the local directory. 
# If nothing is entered, or the filename is not found, a default .txt file will be opened.
# If the user's file is found in the directory, the user's file will be opened instead.
def readTextFile():
    text_file = "reid3.txt"
    user_file = input("\nPlease enter a the name of a local .txt document, in this directory, to edit.\nPress enter for default. ")
    if os.path.isfile(user_file):
        text_file = user_file
        print(f"{user_file} found. Opening the file.\n")
    elif os.path.isfile(user_file + ".txt"):
        text_file = user_file + ".txt"
        print(f"{user_file}.txt found. Opening the file.\n")
    else:
        print("Opening the default file reid3.txt.\n")

    with open(text_file, "r+") as text:
        content = text.read()
        print(content, "\n")

    return content


# Sets the menu items based and asks for user selection, which is returned to main to run the requested function
def editMenu():
    choices = {1: ["Top 5 most common words", allWordCount], 2: ["Single Word Frequency", singleWordCount], 3: ["Replace a word", replaceWord], 
               4: ["Add Text", addText], 5: ["Delete Text", deleteText], 6: ["Highlight Text", highlight], 
               7: ["Ransom Letter", ransomText], 8: ["Exit"]}
    for c in choices:
        print(f"{c}: {choices[c][0]}")

    try:
        user_choice = int(input("Please make a selection: "))
        if user_choice not in choices:
            (print("\n\033[31mYou have made an invalid selection. Please try again.\033[0m\n")) 
        else:
            return choices[user_choice]  
    except ValueError:
        print("\n\033[31mPlease enter a valid number.\033[0m\n")


# Function to clean the text for counting purposes
def clean_text(content):
    # remove punctuation from the text
    no_punctuation = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    content = content.translate(no_punctuation)
    # remove new line (\n) from the text
    content = content.replace("\n", " ")
    content = content.lower()
    # separate the words into a dictionary 
    words = content.split()

    return words


# Function to count the top five words in the text
def allWordCount(content):
    word_count = dict()
    words = clean_text(content)

    try:
        # count the words
        for word in words:
            word_count[word] = word_count.get(word,0) + 1
        # sorth the words by highest count to lowest count
        dict_sort = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
        word_sort = dict(dict_sort)
        # Take the counts and put the top five values in a sorted set
        lst = list(word_sort.values())
        set_list = (sorted(set(lst), reverse=True))[:5]
        # Calculates a total number of words and total unique words
        lst_sum = sum(lst)
        print(f"There are {lst_sum} total words in the text, of which {len(word_sort)} are unique.\n")

        # if a word in the text has a count that matches the top five values, 
        # print out the word and number of times it appears
        for count in word_sort:
            if word_sort[count] in set_list:
                print(f"The word \'{count}\' appears {word_sort[count]} times in the text.")

    except Exception as e:
        print(e)

    
# Counts the frequency of a specified word
def singleWordCount(content):
    user_word = " "
    # Run a check that only one word was entered
    while " " in user_word:
        user_word = input("What word would you like to check for? ")
        if " " not in user_word:
            break
        else:
            print("\nPlease enter only one word per request.\n")
    word_count = dict()
    words = clean_text(content)

    # Make a count of words for the user specified words and present the total count.
    for word in words:
        if word == user_word.lower():
            word_count[word] = word_count.get(word,0) + 1
    if word_count:
        for word in word_count:
            print(f"\nThe word \'{word}\' appears {word_count[word]} times in the text.\n")
    else:
        print(f"\nThe word \'{user_word}\' was not found in this text.\n")
    

# Function to save any changes upon user request
def saveTextFile(new_content):
    # Ask the user if they want to save the modified content to a new file
    save_option = input("Would you like to save this as a new file? (yes/no): ").strip().lower()
    
    if save_option == "yes" or save_option == "y":
        filename = input("Enter the filename (without extension): ").strip()
        # Save the replaced content as a .txt file
        try:
            with open(f"{filename}.txt", "w") as file:
                file.write(new_content)
            print(f"\nThe content has been saved as {filename}.txt.\n")
        except Exception as e:
            print(f"An error has occurred:\n{e}\n")
    else:
        print("\nThe file was not saved.\n")


# Function to replace an existing word with one specified by the user
def replaceWord(content):
    old_word = input("What word would you like to replace?  ")
    new_word = input(f"What word would you like to use instead of {old_word}?  ")
    # Replace the old word with the new word
    pattern = r"\b" + re.escape(old_word) + r"\b"
    replaced_content = re.sub(pattern, new_word, content, flags=re.IGNORECASE)

    # Count the number of words replaced
    word_count = dict()
    # Handles usecase of the replaced word being a punctuation mark
    if new_word in string.punctuation:
        words = clean_text(content)
        # Make a count of words for the user specified words and present the total count.
        for word in words:
            if word == old_word.lower():
                word_count[word] = word_count.get(word,0) + 1
    # Standard replacement of old word for new word
    else:
        words = clean_text(replaced_content)
        # Make a count of words for the user specified words and present the total count.
        for word in words:
            if word == new_word.lower():
                word_count[word] = word_count.get(word,0) + 1

    if word_count:
        for word in word_count:
            print(f"\nThe word \'{old_word}\' was replaced with \'{new_word}\' {word_count[word]} times in the text.\n")
    else:
        print(f"\nThe word \'{old_word}\' was not found in this text.\n")

    print(f"\n{replaced_content}\n")
    saveTextFile(replaced_content)


# Function adds text to the existing text
def addText(content):
    location = 0
    while location != 1 or location != 2:
        try:
            location = int(input("Would you like to add text to 1. The beginning of the original text or 2. The end of the original text?  "))
            if location == 1 or location == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("\n\033[31mPlease enter a valid number.\033[0m\n")
        
    new_text = input("what would you like to add?  ")
    # Puts new text at the beginning or the end of the original based on user selection
    if location == 1:
        edited_content = new_text + " " + content
    elif location == 2:
        edited_content = content + " " + new_text
    else: 
        print("\n\033[31mYou have made an invalid selection.\033[0m\n")
        edited_content = content

    print(f"\n{edited_content}\n")
    saveTextFile(edited_content)


# Function to ask user for a word and delete its first occurrence 
def deleteText(content):
    user_word = " "
    # Run a check that only one word was entered
    while " " in user_word:
        user_word = input("What word would you like to remove?  ")
        if " " not in user_word:
            break
        else:
            print("\nPlease enter only one word per request.\n")
    # Find word to delete and replace it with an empty string, then remove any spacing.
    pattern = r"\b" + re.escape(user_word) + r"\b"
    edited_content = re.sub(pattern, "", content, count=1, flags=re.IGNORECASE)
    edited_content = re.sub(r"\s{2,}", " ", edited_content).strip()

    print(f"\n{edited_content}\n")
    saveTextFile(edited_content)


# Function to highlight specified word using "**"
def highlight(content):
    old_word = input("What word would you like to hilight?  ")
    new_word = "**" + old_word + "**"
    # Replace the old word with the new word
    pattern = r"\b" + re.escape(old_word) + r"\b"
    replaced_content = re.sub(pattern, new_word, content)
    
    # Print a statement if the word is not found
    words = clean_text(content)
    if old_word not in words:
        print(f"\nThe word \'{old_word}\' was not found in this text.\n")

    print(f"\n{replaced_content}\n")
    saveTextFile(replaced_content)   


# Function to change text into a fun ransom letter format. 
def ransomText(content):
    ransom = []
    plain = []
    upper = True
    color = True
    print("\nTurning your text into a ransom letter.\nDonations are appreaciated if you collect.\n")
    for word in content:
        if word.isalpha():
            if upper:
                case_char = word.upper()
            else:
                case_char = word.lower()

            # Alternate color and append to version for displaying in terminal window
            if color:
                ransom.append(f"\033[31m{case_char}\033[0m") 
            else:
                ransom.append(f"\033[35m{case_char}\033[0m") 

            # Append the plain version for saving to a txt file
            plain.append(case_char)

            # Toggle case and color
            upper = not upper
            color = not color

        else:
            ransom.append(word)
            plain.append(word)

    ransom_letter = "".join(ransom)
    plain_letter = "".join(plain)
    print(f"\n{ransom_letter}\n")
    saveTextFile(plain_letter)


# Main function to run the program
def main():
    content = readTextFile()

    while True:
        user_choice = False
        while not user_choice:
            user_choice = editMenu()
        print(f"\n\033[32m{user_choice[0]}\033[0m\n")

        if user_choice[0] != "Exit":
            try:
                user_choice[1](content)
            except (IndexError, TypeError) as e:
                print(f"\n\033[31mIndex error has occurred.\n{e}\nPlease try again or make another selection.\033[0m\n")
        else:
            print("\n\033[32mI hope you enjoyed the text editor.\nPlease come again soon.\033[0m\n")
            break


if __name__ == "__main__":
    main()