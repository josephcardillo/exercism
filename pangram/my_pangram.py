import re

def is_pangram(sentence):
    non_letters = r'[^a-z]'
    # Remove duplicates with set, and make lowercase:
    remove_dupes = "".join(set(sentence)).lower()
    print(f"remove_dupes = {remove_dupes}")
    # Sort a from a - z:
    sort_string = "".join(sorted(remove_dupes))
    print(f"sort_string = {sort_string}")
    # Remove non-letters from b:
    just_letters = re.sub(non_letters, "", sort_string)
    if just_letters.lower() == "abcdefghijklmnopqrstuvwxyz":
        print(f"just_letters = {just_letters}")
        print(True)
        # return True
    else:
        print(f"just_letters = {just_letters}")
        print(False)
        # return False

test1 = "the quick brown fox jumps over the lazy dog"
test2 = "a quick movement of the enemy will jeopardize five gunboats"
test3 = "7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"
test4 = "the_quick_brown_fox_jumps_over_the_lazy_dog"
test5 = '"Five quacking Zephyrs jolt my wax bed."'

is_pangram(test1)
is_pangram(test2)
is_pangram(test3)
is_pangram(test4)
is_pangram(test5)