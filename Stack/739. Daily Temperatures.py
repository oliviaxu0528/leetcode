# Daily Temperatures - Monotonic Stack - Leetcode 739 - Python
def dailyTemperatures(temperatures):
    l = len(temperatures)
    res = [0] * l
    for i in range(1, l+1):
        for j in range(0, l-i):
            if temperatures[i]>temperatures[i-1]:
                res[i-1] = temperatures[i]-temperatures[i-1]
                break



temperatures = [73,74,75,71,69,72,76,73]
dailyTemperatures(temperatures)