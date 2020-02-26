d=list(map(int,input().split(',')))
s=[]
for i in d:
	for i in range(1,i+1):
		Q=(10*i/3)**0.5
	s.append(int(Q))
print(*s,sep=',')
