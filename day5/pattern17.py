def x(n):
    for i in range(n):
        for j in range(n):
            if i==j or j==n-i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
   

def main():
    n=int(input())
    x(n)

if __name__=="__main__":
    main()