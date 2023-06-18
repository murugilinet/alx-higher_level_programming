#!/usr/bin/python3
output = ""
for character in range(97, 123):
    if character != 101 and character != 113:
        output += "{:c}".format(character)
print(output, end="")
