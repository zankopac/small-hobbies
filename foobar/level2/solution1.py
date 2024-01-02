def solution(n, b):
    #Your code here

    def toBase(n,base):
        convertString = "0123456789ABCDEF"
        if n < base:
            return convertString[n]
        else:
            return toBase(n//base,base) + convertString[n%base]

    nodes = []
    while n not in nodes:
        nodes.append(n)
        k = len(n)
        nArr = [x for x in n]
        xArr = sorted(nArr, reverse = True)
        yArr = sorted(nArr, reverse = False)
        x = int(''.join(xArr),b)
        y = int(''.join(yArr),b)
        z = x-y
        z = toBase(z,b)
        kDiff = k-len(z)
        if kDiff > 0:
            z = "0"*kDiff + z
        n = z
       # print(nodes)
        #print(n)

    result = len(nodes) - nodes.index(n)
    return result
    
print(solution('1211', 10))