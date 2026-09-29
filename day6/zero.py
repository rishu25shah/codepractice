def zero(n,arr):
    new=[]
    for i in arr:
        if i!=0:
            new.append(i)
    for i in arr:
        if i==0:
            new.append(i)
    
    return new
        



def main():
    n=8
    arr=[4,5,0,1,9,0,5,0]
    result=zero(n,arr)
    print(result)

if __name__=="__main__":
    main()