def triangle01(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2==0:
                print("1",end="")
            else:
                print("0",end="")
        print()
def main():
    n=int(input())
    triangle01(n)
if __name__=="__main__":
    main()