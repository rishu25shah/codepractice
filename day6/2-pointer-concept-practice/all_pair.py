arr=[1,2,3,4,5,6,7]
target=9
left=0
pair=[]
right=len(arr)-1
while left < right:
    total=arr[left]+arr[right]
    if total==target:
        pair.append([arr[left],arr[right]])
        left+=1
        right-=1
    elif total > target:
        right-=1
    else:
        left+=1
print(pair)
