def ispalindrome(S):
    S=S.replace(" ","")
    S=S.replace(",","")
    S=S.replace(":","")
    S=S.lower()
    print(S)

    left=0
    right=len(S)-1
    while left<=right:
        if S[left]==S[right]:
            left+=1
            right-=1
        else:
            print("string is not palindrone")
            return
    print("string is palindrome")

    

S = " "
ispalindrome(S)

#import re
#def isPalindrome(self, s):
 #       new_s = re.sub(r"[^a-zA-Z0-9\\s+]", "", s).lower()
  #      return new_s == new_s[::-1]