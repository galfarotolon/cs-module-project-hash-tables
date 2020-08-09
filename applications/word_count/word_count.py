def word_count(s):
    # Your code here
    characters_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    for character in characters_to_ignore:
        s = s.replace(character, "")

    d = {}

    words = s.split()

    for word in words:
        word = word.lower()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))