import sys

if len(sys.argv) >= 2:
    s = " ".join(sys.argv[1:])
else:
    s = level

filtered = ""
for ch in s:
    if ch.isalnum():
        filtered += ch.lower()

if filtered == filtered[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
