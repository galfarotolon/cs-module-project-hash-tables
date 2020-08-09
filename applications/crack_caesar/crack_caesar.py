# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here


with open(r"C:\Users\galfa\Desktop\CODING\Lambda\unit-6\week-1\cs-module-project-hash-tables\applications\crack_caesar\ciphertext.txt") as f:
    words = f.read()

    print(words)


def crack_caesar(coded_message):
    letter_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    count = {}
    key = {}
    deciphered = ''

    for char in coded_message:
        if char in letter_frequency:
            if count.get(char) is None:
                count[char] = 1
            else:
                count[char] = count[char] + 1

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(letter_frequency)):
        key[sorted_count[i][0]] = letter_frequency[i]

    for c in coded_message:
        if c in letter_frequency:
            deciphered += key[c]
        else:
            deciphered += c

    return deciphered

print(crack_caesar(words))
