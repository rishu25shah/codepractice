def valid(par):
    stack=[]
    for i in par:
        if i in ["(","{","["]:
            stack.append(i)
        elif i==")" and len(stack)>0 and stack[-1]=="(":
                stack.pop()                                         
        elif i=="}" and len(stack)>0 and stack[-1]=="{":
            stack.pop()
        elif i=="]" and len(stack)>0 and stack[-1]=="[":
            stack.pop() 
        elif i in [")","}","]"]:
            return False
        
    return len(stack)==0  

def main():
    par=input("Enter the parentheses string: ")
    result=valid(par)
    print(result)

if __name__=="__main__":
    main()