def anagrams(str1,str2):
    frequency1={}
    frequency2={}
    for char in str1:
        if char in frequency1:
            frequency1[char]+=1
        else:
            frequency1[char]=1

    for char in str2:
            if char in frequency2:
                frequency2[char]+=1
            else:
                frequency2[char]=1
    
    if frequency1==frequency2:
        print("anagrams")
    else:
        print("not anagrams")



def main():
    str1="listen"
    str2="hello"
    anagrams(str1,str2)


if __name__=="__main__":
    main()