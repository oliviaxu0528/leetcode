from collections import Counter
def checkInclusion(s1,s2):
    cntr, w, match = Counter(s1),len(s1),0
    for i in range(len(s2)):
        if s2[i] in cntr:
            if not cntr[s2[i]]: match -=1
            print("i1:", i)
            print("match1:", match)
            cntr[s2[i]] -=1
            if not cntr[s2[i]]: match +=1
            print("i2:", i)
            print("match2:", match)
            print("cntr111: ", cntr)   

        if i>=w and s2[i-w] in cntr:
            if not cntr[s2[i-w]]: match -=1
            print("i3:", i)
            print("match3:", match)
            cntr[s2[i-w]] +=1
            if not cntr[s2[i-w]]: match +=1
            print("i4:", i)
            print("match4:", match)

        if match == len(cntr):
            print("cntr2222: ", cntr)
            return True
    return False

s1 = "abc"
s2 = "caddbcc"
print(checkInclusion(s1,s2))
                
    