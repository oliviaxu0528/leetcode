from collections import Counter
def checkInclusion(s1,s2):
    cntr, w, match = Counter(s1),len(s1),0
    for i in range(len(s2)):
        if s2[i] in cntr:
            # print("match1: ", match)
            if not cntr[s2[i]]: match -=1
            
            print("cntr: ",cntr)
            cntr[s2[i]] -=1
            print("cntr2: ",cntr)
            if not cntr[s2[i]]: match +=1

        if i>=w and s2[i-w] in cntr:
            if not cntr[s2[i-w]]: match -=1
            cntr[s2[i-w]] +=1
            if not cntr[s2[i-w]]: match +=1

        if match == len(cntr):
            return True
    return False

s1 = "ab"
s2 = "cadba"
print(checkInclusion(s1,s2))
                
    