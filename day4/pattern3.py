def reverserightangletriangle(n):
    for i in range(n,-1,-1):
        for j  in range(i+1):
            print("*",end="")
        print()

def main():
    n=int(input())
    reverserightangletriangle(n)

if __name__=="__main__":
    main()