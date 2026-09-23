def move_zero(number):
    new=[]
    for i in number:
        if i != 0:
            new.append(i)
    for i in number:
        if i ==0:
            new.append(i)
    return new        

    

def main():
    number=[0,1,0,3,12]
    result=move_zero(number)
    print(result)

if __name__=="__main__":
    main()