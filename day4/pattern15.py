def hollowinvertedpyramid(n):
    for i in range(n-1,-1,-1):
        spaces=n-i
        print(" "*spaces,end="")
        for j in range(2*i+1):
            if i==n-1 or j==0 or j==2*i:
                print("*",end="")
            else:
                print(" ",end="")
        print() 

def main():
    n=int(input())
    hollowinvertedpyramid(n)

if __name__=="__main__":
    main()