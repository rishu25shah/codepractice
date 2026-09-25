def watercontainer(height):
    new=[]
    area=0
    width=0
    for i in range (len(height)):
        left_height=height[i]
        for j in range(len(height)-1,-1,-1):
            right_height=height[j]
            if i<j:
                water_height=min(left_height,right_height)
                width=j-i
                current_area=water_height*width
                area=max(area,current_area)
    return area

def opwater(height):
    left=0
    right=len(height)-1
    area=0
    while left<right:
        water_height=min(height[left],height[right])
        width=right-left
        current_area=water_height*width
        area=max(current_area,area)
        if height[left]>height[right]:
            right-=1
        else:
            left+=1

    return area                
def main():
    height=[1,8,6,2,5,4,8,3,7]
    result=watercontainer(height)
    result1=opwater(height)
    print(result)
    print(result1)

if __name__=="__main__":
    main()