def triangle(n):
    for i in range(n):
        spaces=n-i+1
        star=2*i+1
        print(" "*spaces,end="")
        print("*"*star)
        

def main():
    n=int(input())
    triangle(n)

if __name__=="__main__":
    main()