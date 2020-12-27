import re

def is_pangram(sentence):
    # Use regex to specify all non-letters:
    non_letters = r'[^a-z]'
    # Remove duplicates with set, and make lowercase:
    remove_dupes = "".join(set(sentence)).lower()
    # Sort remove_dupes from a - z:
    sort_string = "".join(sorted(remove_dupes))
    # Remove non-letters from sort_string:
    just_letters = re.sub(non_letters, "", sort_string)
    if just_letters.lower() == "abcdefghijklmnopqrstuvwxyz":
        return True
    else:
        return False
