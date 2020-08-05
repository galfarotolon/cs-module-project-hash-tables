def no_dups(s):
    # Your code here

    dupe_count = 0
    words = {}
    space = ' '
    
    string_split = s.split()

    for word in string_split:
        if word in words:
            continue
        else:
            dupe_count += 1
            words[word] = dupe_count
    
    return space.join(words.keys())



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))