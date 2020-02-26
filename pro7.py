h=10
r=5
f=15
Vtank=3.14*(r)**2*h
t=int(input('Enter time='))
Vwater=f*t
if Vwater>Vtank:
	print('Overflow')
	print('Volume',Vwater-Vtank)
elif Vwater==Vtank:
	print('Fill')
else:
	print('Underflow')
	ht=Vwater/(3.14*(r)**2)
	hr=h-ht
	print('Filled height=',round(ht,2),'Remaining height=',round(hr,2))
