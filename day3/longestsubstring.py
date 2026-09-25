def long(s):
    l=0
    max1=0
    seen=set()
    for i in range(len(s)):
        while s[i]  in seen:
            seen.remove(s[l])
            l+=1
        seen.add(s[i])
        current_length=i-l+1
        max1=max(current_length,max1)
    return max1



def main():
    s="abcabcbb"
    result=long(s)
    print(result)
if __name__=="__main__":
    main()
