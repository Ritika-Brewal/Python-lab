h=eval(input())
if len(h)==0:
	print('Empty')
for i in h:
	if type(i) not in [int,float]:
		print('No')
		break
else:
	print('Yes')
