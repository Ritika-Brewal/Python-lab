t=(3,4,7,8,3,0,7,8)
b=[]
for i in t:
	if t.count(i)>1 and i not in b:
		print(i,'is repeated element')
		b.append(i)
