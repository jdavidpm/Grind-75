def isPalindrome(self, s: str) -> bool:
	s = "".join([c.lower() for c in s if c.isalpha() or c.isdigit()])
	return True if (s == s[::-1]) else False
