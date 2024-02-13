# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]

s = "500"
ans = isPalindrome(s)

if ans:
	print("This is a palindrome")
else:
	print("This is not a palindrome")


isPalindrome(s)


