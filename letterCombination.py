class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans = []
        
        if len(digits) == 0: return ans
   
        self.solve(digits,buttons,ans)
        return ans
    
    def solve(self, digits, buttons, ans, current_string="",current_level = 0):
        if current_level == len(digits):
            ans.append(current_string)
            return
        for i in buttons[int(digits[current_level])]:
            self.solve(digits,buttons,ans,current_string+i,current_level+1)
