class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        n_list = []

        for i in s:
            if i.isalnum():
                s_list.append(i.lower())

        for i in s_list:
            if i.isalnum() and i != " ":
                n_list.insert(0, i.lower())

        return s_list == n_list