def solution(i):
    # Your code here
    
    def isPrime(a):
        # Check if the number is less than
        # or equal to 1, return False if it is
        if a <= 1:
            return False
        # Loop through all numbers from 2 to
        # the square root of n (rounded down to the nearest integer)
        for i in range(2, int(a**0.5)+1):
            # If n is divisible by any of these numbers, return False
            if a % i == 0:
                return False
        # If n is not divisible by any of these numbers, return True
        return True
        
    strlensum = 0
    iPrimeIndex = 0
    primesArr =  []
    strlensumArr = []
    n = 2
    while strlensum < i:
        if isPrime(n):
           # print(n)
            strlen = len(str(n))
            strlensum = strlensum + strlen
            primesArr.append(str(n))
            strlensumArr.append(strlensum)
            iPrimeIndex = i-strlensum
        n = n + 1
    
    primesArrStr = ''.join(primesArr)
    res = ""
    if i < len(primesArrStr):
        res = primesArrStr[i:]
    if len(primesArr) > 0:
        iPrime = str(primesArr[(len(primesArr)-1)])
        #res = res + iPrime[iPrimeIndex:]
    else:
        iPrime = 0
    n = int(iPrime) + 1
    while len(res) < 5:
        if isPrime(n):
            res = res + str(n)
        n = n + 1
            
    return res[:5]


print(solution(10000))