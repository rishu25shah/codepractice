def numbertriangle(n):
    for i in range(n):
        for j  in range(i+1):
            print(j+1,end="")
        print()

def main():
    n=int(input())
    numbertriangle(n)

if __name__=="__main__":
    main()