
def first_duplicate(word):
    frequency={}
    for  i in word:
        if i in frequency:
            frequency[i]+=1
            if frequency[i] > 1:
                print(i)
                break
        else:
            frequency[i]=1
            

    
        

def main():
    word="programming"
    first_duplicate(word)



if __name__ == "__main__":
    main()