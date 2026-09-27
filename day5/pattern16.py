def upperbutterfly(n):
    for i in range(n):
       left_star=i+1
       right_star=i+1
       spaces=2*(n-i-1)
       print("*"*left_star+" "*spaces+"*"*right_star)
               
def lowerbutterfly(n):
    for i in range(n-1,-1,-1):
        left_star=i
        right_star=i
        spaces=2*(n-i)
        print("*"*left_star+" "*spaces+"*"*right_star)
       

    




def main():
    n=int(input())
    upperbutterfly(n)
    lowerbutterfly(n)


if __name__=="__main__":
    main()