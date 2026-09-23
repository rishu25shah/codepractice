def kfrequency(nums,k):
    f={}
    for num in nums:
        if num in f:
            f[num]+=1
        else:
            f[num]=1
    new=[]
    while k>0:
        max_key=max(f,key=f.get)
        new.append(max_key)
        del f[max_key]
        k-=1
    return new
            


def main():
    nums=[1,1,1,2,2,3]
    k=2
    result=kfrequency(nums,k)
    print(result)

if __name__=="__main__":
    main()