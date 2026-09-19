class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        result = []

        for word in strs:
            key = "".join(sorted(word))
            
            if key in freq:
                freq[key].append(word)
            else:
                freq[key] = [word]
        
        for k in freq.values():
            result.append(k)
        return result
