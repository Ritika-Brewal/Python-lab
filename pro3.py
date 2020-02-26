lst=list(map(int,input().split(',')))
s=[]
for i in lst:
	fact=1
	for i in range(1,i+1):
		fact*=i
	s.append(fact)
print(*s,sep=',')
