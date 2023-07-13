def checkprofit(S):

    l=len(S)
    
    max_profit=0
    buy=0
    
    while buy<l:
        sell=buy+1
        while sell<l:
            d=S[sell]-S[buy]
            if d>max_profit:
                max_profit=d
            sell+=1
        buy+=1

    print("MAXIMUM PROFIT = ",max_profit)


prices = [7,1,5,3,6,4]
checkprofit(prices)
