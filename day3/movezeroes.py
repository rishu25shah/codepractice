def moveZeroes(nums):
    k=0
    temp=0

    for i in range(len(nums)):
        if nums[i] != 0:
            temp=nums[i]
            nums[i]=nums[k]
            nums[k]=temp
            k+=1
    return nums
    

    


        
        


def main():
    nums=[0, 1, 0, 3, 12]
    result=moveZeroes(nums)
    print(result)
 
if __name__=="__main__":
    main()  