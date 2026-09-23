def contain_duplicate(number):
    fre={}
    for i in number:
        if i in fre:
            fre[i]+=1
            if fre[i]>1:
                return True
        else:
            fre[i]=1
    return False    

def main():
    number=[1,2,3]
    result=contain_duplicate(number)
    print(result)

if __name__=="__main__":
    main()