def rightangletriangle(n):
    for i in range(n):
        for j  in range(i+1):
            print("*",end="")
        print()

def main():
    n=int(input())
    rightangletriangle(n)

if __name__=="__main__":
    main()