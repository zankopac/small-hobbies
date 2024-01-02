import sys
def solution(nStart):
    def halveAsString(n):
        res = ""
        carry = 0
        for i in range(len(n)):
            d = int(n[i])
            if carry == 1:
                d = d + 10
            carry = d%2
            res = res + str(d//2)
        return removeFrontZeros(res)
    def removeFrontZeros(n):
        if n.startswith("0"):
            n = n[1:]
            return removeFrontZeros(n)
        else:
            return n
        
    def add1AsString(n):
        res = list(n)
        for i in reversed(range(len(n))):
            d = n[i]
            newD = int(d) + 1

            if newD < 10:
                res[i] = str(newD)
                break
            else:
                res[i] = "0"
                if i == 0:
                    res = ["1"]+res
                continue
        return  removeFrontZeros("".join(res))
    def subtract1AsString(n):
        res = list(n)
        for i in reversed(range(len(n))):
            d = n[i]
            newD = int(d) - 1

            if newD > -1:
                res[i] = str(newD)
                break
            else:
                res[i] = "9"
                continue
        return removeFrontZeros("".join(res))

    checked = {}
    def rec(n, count):
        if n in checked.keys():
            return checked[n]
        if n == "1":
            return count
        count = count + 1
        if n[len(n)-1] in ["0","2","4","6","8"]:
            return rec(halveAsString(n), count)
        else:
            nAdd = add1AsString(n)
            resAdd = rec(nAdd,count)
            checked[nAdd] = resAdd
            nSubtract = subtract1AsString(n)
            resSubtract = rec(nSubtract,count)
            checked[nSubtract] = resSubtract
            return resAdd if resAdd < resSubtract else resSubtract
    
    return rec(nStart, 0)
sys.setrecursionlimit(2000)
print(solution("153543523656325362357346443263476835673523146478478637525321421153543523656325362357346443263476835673523146478478637525321421153543523656325362357346443263476835673523146478478637525321421153543523656325362357346443263476835673523146478478637525321421214211535435563253623573464432634768356735231464784786375"))


