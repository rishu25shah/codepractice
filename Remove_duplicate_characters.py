def Remove_duplicate_char(word):
    new = ""

    for char in word:
        if char not in new:
            new += char

    print(new)


            


def main():
    word="programming"
    Remove_duplicate_char(word)


if __name__=="__main__":
    main()