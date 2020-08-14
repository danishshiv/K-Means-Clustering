import random 
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
    res.sort()
    return res
print(Rand(1,500,10))
