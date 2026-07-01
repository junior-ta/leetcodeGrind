class Solution:
    def __init__(self, s):
        self.s= s

    def isPalindrome(self, s: str) -> bool:
        l_ptr = 0
        r_ptr = len(s) - 1
        s = s.lower()

        while r_ptr > l_ptr:
            if s[l_ptr].isalnum() == False:
                l_ptr += 1
                continue

            if s[r_ptr].isalnum() == False:
                r_ptr -= 1
                continue

            if s[l_ptr] != s[r_ptr]:
                return False

            l_ptr += 1
            r_ptr -= 1

        return True

if __name__ == '__main__':
    sln=Solution("ebbe! !")
    print(sln.isPalindrome("ebbe! !"))