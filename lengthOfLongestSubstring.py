class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        lengths = []
        index = 0
  
        for letter in s: # a b c a b c b b
            counter = index

            while letter not in substring: # a
                substring += letter # a ab abc |
                counter += 1 
                if counter != len(s): letter = s[counter]                

            lengths.append(len(substring))
            substring = ""
            index += 1
            
        return max(lengths) if len(lengths) > 0 else 0
