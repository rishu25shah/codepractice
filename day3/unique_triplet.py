def threesum(nums):
    new=[]
    total=0
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
       
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total<0:
                left+=1
            elif total>0:
                right-=1
            else:
                new.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
    return new




def main():
    nums = [-4, -1, -1, 0, 1, 2]
    result=threesum(nums)
    print(result)

if __name__=="__main__":
    main()