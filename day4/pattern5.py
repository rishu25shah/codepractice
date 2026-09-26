def commonnumbertriangle(n):
    for i in range(n):
        for j  in range(i+1):
            print(i+1,end="")
        print()

def main():
    n=int(input())
    commonnumbertriangle(n)

if __name__=="__main__":
    main()