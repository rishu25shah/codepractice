def maxprofit(prices):
    min_price=prices[0]
    profit=0
    for i in range(1,len(prices)):
        current_price=prices[i]
        if current_price < min_price:
            min_price=current_price
        current_profit=prices[i]-min_price
        profit=max(profit,current_profit)
    return profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    result=maxprofit(prices)
    print(result)

if __name__=="__main__":
    main()