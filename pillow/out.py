a = 0

while(a<1):
	print("Enter number of scores: ")
	a= int(input())
b = 0

s = 0

print("Enter one value at a time: ")
while(b<a):
	c= int(input())
	s = s+c

	b = b+1

print("Average: ")
print(float(s/a))