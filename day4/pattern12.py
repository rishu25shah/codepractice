def floydtriangle(n):
    k=1
    for i in range(n):
        for j in range(i+1):
            print(k,end="")
            k+=1
        print()
def main():
    n=int(input())
    floydtriangle(n)
if __name__=="__main__":
    main()   