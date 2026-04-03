class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        i = 0
        while i < len(strs):
            temp_list = [strs[i]]
            j = i + 1
            while j < len(strs):
                if Counter(strs[i]) == Counter(strs[j]):
                    temp_list.append(strs[j])
                    del strs[j]
                else:
                    j += 1
            anagram_list.append(temp_list)
            i += 1
        return anagram_list