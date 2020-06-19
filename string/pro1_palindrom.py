ch= raw_input("Enter your string")
print (ch)

'''if (isPalindrome(ch) == 1):
    print( "palindrome ispalindrome()")
else:
    print("not palindrome")
'''
rev_ch=ch[::-1]
print (rev_ch)

if rev_ch == ch:
    print("String is palindrom:")
else:
    print("not palindrom")
