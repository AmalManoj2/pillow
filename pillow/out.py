a = 2

b = 2

c = 0

d = 0

check = 1

number = 0

prime = 0

print("Enter number of primes: ")

number= int(input())
while(check):
	while(b<=a/2):
		c = a/b

		while(c>0):
			c = c-1

		if(c==0.0):
			d = 1

		b = b+1

	if(d==0):
		print(float(a))
		prime = prime+1

	d = 0

	a = a+1

	if(prime==number):
		check = 0

