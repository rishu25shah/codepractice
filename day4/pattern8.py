def Inverted_Pyramid(n):
    for i in range(n-1,-1,-1):
        stars=2*i+1
        spaces=n-i-1

        print(spaces*" ",end="")
        print(stars*"*")
def main():
    n=int(input())
    Inverted_Pyramid(n)


if __name__=="__main__":
    main()