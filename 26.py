# 26.py
p=int(input())
f=list(map(int,input().split()[:p]))
f.sort()
for v in f:
   print(v,end=" ")
   
