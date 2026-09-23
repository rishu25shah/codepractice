def ans(s,t):
    f1={}
    f2={}
    for i in s:
        if i in f1:
            f1[i]+=1
        else:
            f1[i]=1
    for i in t:
        if i in f2:
            f2[i]+=1
        else:
            f2[i]=1
    if f1==f2:
        return True
    else:
        return False

def main():
    s="anagram"
    t="nagaram"
    result=ans(s,t)
    print(result)

if __name__=="__main__":
    main()