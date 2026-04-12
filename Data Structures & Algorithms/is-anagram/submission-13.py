class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_t = list(t)
        
        if len(s) != len(t):
            return False

        for i in s:
            if i != (len(s) + 1):
                if i in check_t:
                    check_t.remove(i)
                else:
                    return False
            else:
                break
        return True