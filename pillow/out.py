z = 0

x = 0

n = 0

s = 0

w = 0

check = 0

print("Enter length of number: ")

n= int(input())
while(x<n):
	print("Enter each individual digit of the number: ")

	w= int(input())
	z = 0

	s = s*10

	s = s+w

	while(z<x):
		w = w*10

		z = z+1

	x = x+1

	check = check+w

print(float(s))
print(float(check))
if(s==check):
	print("Yes, it is a Palindrome")

if(s!=check):
	print("No, it is not a Palindrome")

