def counte(s):
	c=0
	for j in s:
		if(j in "AEIOU"):
			c+=1
	return c

def minion_game(xs):
	
	k=0
	s=0
	v=counte(xs[0:len(xs)])
	c=len(xs)-v
	for i in range(1,len(xs)+1):
		if(xs[len(xs)-i] in "AEIOU"):
			v-=1
		else:
			c-=1
		k+=v
		s+=c
		
	if(s>k):
		print("Stuart",s)
	elif(s<k):
		print("Kevin",k)
	else:
		print("Draw")
