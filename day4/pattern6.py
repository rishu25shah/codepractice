def rightalignedtriangle(n):
    for i in range(n-1,-1,-1):
        print(i*" ",end="")            
        for j in range(n-i):
            print("*",end="")    
        print()

def main():
    n=int(input())
    rightalignedtriangle(n)

if __name__=="__main__":
    main()