l=[]
while 1:
	item=input('Enter the item=')
	l.append(item)
	n=input('Do you want to continue y/n')
	if n.lower()=='n':
		break
print(l)
