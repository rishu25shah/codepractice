def rombus(n):
    for i in range(n,-1,-1):
        spaces=i
        stars=n
        print(" "*spaces,end="")
        print("*"*stars)

def main():
    n=int(input())
    rombus(n)

if __name__=="__main__":
    main()