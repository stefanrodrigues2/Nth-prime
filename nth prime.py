def prime(n):
	if(n==0):
		return
	count =0
	for i in xrange(2,1000):
		flag =1
		for j in range(2,(i/2)+1):
			if ( i % j ==0):
				flag  =0
				break
		if flag:
			count +=1
		if(count == n):
			break
	print i

n = int(input("Enter number:"))
prime(n)

