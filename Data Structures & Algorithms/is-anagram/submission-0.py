class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for m in t:
            if m in t_dict:
                t_dict[m] += 1
            else:
                t_dict[m] = 1
        return s_dict == t_dict