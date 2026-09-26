def upperdiamond(n):
    for i in range(n):
        stars=2*i+1
        spaces=n-i-1
        print(" "*spaces,end="")
        print("*"*stars)
def lowerdiamond(n):
    for j in range(n-2,-1,-1):
        stars1=2*j+1
        spaces1=n-j-1
        print(" "*spaces1,end="")
        print("*"*stars1)

def main():
    n=int(input())
    upperdiamond(n)
    lowerdiamond(n)

if __name__=="__main__":
    main()