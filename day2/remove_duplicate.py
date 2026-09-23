def remove_duplicate(nums):
    fre={}
    for i in nums:
        if i in fre:
            fre[i]+=1
        else:
            fre[i]=1
    return len(fre)


def main():
    nums=[1,1,2]
    result=remove_duplicate(nums)
    print(result)

if __name__=="__main__":
    main()