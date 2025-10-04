# approach: two pointer
def palindrome_substring(s):
    length,substring = 0,''
    for i in range(len(s)):
        # for odd length, we start at one index, and pan out from both directions
        r,l = i,i # aba
    # both l and r start from a single pos, l goes left and r goes right
        while r<len(s) and s[r]==s[l] and l>=0:
            if (r-l+1) > length:
                length = r-l+1
                substring = s[l:r+1]
            l-=1
            r+=1

        # for even length: abba
        l,r = i,i+1
        while r<len(s) and s[r]==s[l] and l>=0:
            if (r-l+1) > length:
                length = r-l+1
                substring = s[l:r+1]
            l-=1
            r+=1

    return substring

s = input()
print(palindrome_substring(s))
print(len(palindrome_substring(s)))




