# postive always runnung sum

arr = [-4,3,2,1]
x=5

def minstart(arr):
    min_n=0
    sum_n=0
    for i in arr:
        sum_n+=i
        min_n=min(sum_n,min_n)
        
        
    return 1-min_n

# minstart(arr=arr)


# Tempreture prediction

# necessary import libraries
# import numpy as np
# import datetime,time
# from sklearn.linear_model import LinearRegression

# # dummy inputs (one day)
# data=[10.0,11.1,12.3,13.2,14.8,15.6,16.7,17.5,18.9,19.7,20.7,21.1,22.6,23.5,24.9,25.1,26.3,27.8,28.8,29.6,30.2,31.6,32.1,33.7]
# startDate = '2013-01-01'
# endDate = '2013-01-01'
# p = 1
# n = 1

# # utility function
# def predictTemperature(startDate, endDate, temperature, n):
#     p = int(len(temperature)/24)
#     x = []
#     for i in range(1,((24*p)+1)):
#         x.append(i)
#     y = temperature
#     lm = LinearRegression()
#     lm.fit(np.asarray(x).reshape(-1,1),y)
    
#     f = x[-1]+1
#     z = []
#     for i in range(24*n):
#         z.append(f)
#         f += 1
#     return(lm.predict(np.asarray(z).reshape(-1,1)).tolist())

# # call the utility function
# # print(predictTemperature(startDate, endDate, data, n))

# 3. Divisible strings
s = "bcdbcd"

t = "bcdbcd"
def findSmallestDivisor(s, t):
    # Write your code here
    fits = False
    concat = t
    i=1
    while len(concat)<=len(s):
        if concat!=s:
            i+=1
            concat = t * i
            print(concat)
            print(len(concat))
        else:
            print(concat)
            print(len(concat))
            fits = True
            break
    if not fits:
        return -1
    for i in range(1,len(t)+1):
        if (t[:i]*(len(t)//i)) == t:
            return i


print(findSmallestDivisor(s,t))