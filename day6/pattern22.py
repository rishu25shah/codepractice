def pascals(n):
    for i in range(n):
        spaces=n-i-1
        print(" "*spaces,end="")
        c=1
        for j in range(i+1):
            print(c,end=" ")
            c=c*(i-j)//(j+1)

        print()

def main():
    n=int(input())
    pascals(n)

if __name__=="__main__":
    main()