class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s

        cursor, longest, hashmap = 1, '', {}

        for pivot in range(1, len(s)-1): # 1 2 3           
            print('pivot', pivot, s[pivot], s[pivot-1:pivot+2])
            cursor = 1
            longest = s[pivot]
            while (s[pivot - cursor] == s[pivot + cursor]) and (pivot - cursor != 0) and (pivot + cursor != len(s)):
                longest = s[(pivot - cursor):(pivot + cursor + 1)]                
                cursor += 1              
            hashmap[longest] = len(longest)

        print(hashmap)     
        return max(hashmap, key=hashmap.get)
