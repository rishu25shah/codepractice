def non_repeating_char(word):
    frequency={}
    for char in word:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1

    for i in frequency:
        if frequency[i]==1:
            print(i)
            break

def main():
    word="programming"
    non_repeating_char(word)

if "__name__"==main():
    main()