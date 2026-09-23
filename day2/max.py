def find_max(number):
     max=number[0]
     for i in number:
         if i>max:
             max=i
     return max


def main():
    number=[10,5,20,8,15]
    result=find_max(number)
    print(result)


if __name__=="__main__":
    main()