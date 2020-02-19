l=[]
while 1:
	item=input('Enter item=')
	l.append(item)
	n=input('Do you want to continue y/n=')
	if n.lower()=='n':
		break
l.sort(reverse=True,key=len)
print(l)
