email_string = "bhavishyapriyadarshini9@gmail.com"
char_frequency = {}

for character in email_string:
    if character in char_frequency:
        char_frequency[character] += 1
    else:
        char_frequency[character] = 1

print(char_frequency)