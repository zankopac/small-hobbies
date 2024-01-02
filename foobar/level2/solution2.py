def solution(xs):
    minNegative = 1
    res = 1
    numOfNegative = 0
    numOfPositive = 0
    numOfZero = 0
    isLarge = False
    for x in xs:
        if x == 0:
            numOfZero = numOfZero + 1
            continue
        elif x < 0:
            numOfNegative = numOfNegative + 1
            if x > -1:
                continue
        elif x > 0:
            numOfPositive = numOfPositive + 1
            if x < 1:
                continue
        
        isLarge = True
        res = res*x
        if minNegative == 1 and x <= -1 or x <= -1 and x > minNegative:
            minNegative = x
    
    print(minNegative)
    print(res)
    if numOfZero == len(xs):
        return  "0"
    
    if not isLarge:
        maxDecimal = max(xs)
        minDecimal = min(xs)
        xs.remove(minDecimal)
        minDecimal2 = min(xs)
        return str(max(maxDecimal,minDecimal*minDecimal2))
            


    if numOfNegative == 1 and numOfPositive == 0:
        return "0" if numOfZero > 0 else str(res)

    res = max(res,res/minNegative)

    return str(res)






print(solution([-2,-2,2]))

#print(solution([1,2,3,4,5,6,7,8,9,10]))
#print(solution(range(50)))