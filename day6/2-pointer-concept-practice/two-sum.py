arr=[1,2,3,4,6,8]
target=10
left=0
while left<=len(arr):
    if arr[left]+arr[left+1]==target:
        print(arr[left],arr[left+1])
        break
    else:
        left+=1

        
