a=input()
b=input()
c=0
for i in range(len(a)):
	if a[i:i+len(b)]==b:
		c+=1
print(c)
