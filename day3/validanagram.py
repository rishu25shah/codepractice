def anagram(s,t):
    n1=frequency(s)
    n2=frequency(t)
    if n1==n2:
        return True
    else:
        return False

def frequency(s):
    f={}
    for i in s:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f

def main():
    s="anagram"
    t="nagaram" 
    result=anagram(s,t)
    print(result)

if __name__=="__main__":
    main()
    