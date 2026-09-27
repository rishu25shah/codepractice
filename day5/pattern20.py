def hollowrombus(n):
    for i in range(n):
        spaces=n-i-1
        print(" "*spaces,end="")
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def main():
    n=int(input())
    hollowrombus(n)

if __name__=="__main__":
    main()