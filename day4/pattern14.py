def hollowpyramid(n):
    for i in range(n):
        spaces=n-i-1
        print(" "*spaces,end="")
        for j in range(2*i+1):
            if i==n-1 or j==0 or j==2*i:
                print("*",end="")
            else:
                print(" ",end="")
        print()
        
def main():
    n=int(input())
    hollowpyramid(n)
if __name__=="__main__":
    main()