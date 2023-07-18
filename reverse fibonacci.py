def fiborev():
   k= int(input("enter the upper range"))
   p = [0] * k
   p[0] = 0
   p[1] = 1
   for i in range(2, k): 
      p[i] = p[i - 2] + p[i - 1]
   for i in range(k-1,-1,-1):  
      print(p[i],end=" ")
   return k
fiborev()