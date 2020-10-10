#ID 1591144

user_input: str = input()

def rev_word(user_input):
    for string in user_input.split():
        return " ".join([string[::-1]])

if rev_word(user_input) == user_input:
    print(user_input, "is a palindrome")
elif rev_word(user_input) != user_input:
    print(user_input, "is not a palindrome")



