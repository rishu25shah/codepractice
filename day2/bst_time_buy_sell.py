def maxprofit(prices):
    profit=[]
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<prices[j]:
                profit.append(prices[j]-prices[i])
    num=0
    for i in profit: 
        if i>num:
            num=i
    return num
                    

def main():
    prices=[7,1,5,3,6,4]
    result=maxprofit(prices)
    print(result)   

if __name__=="__main__":
    main()