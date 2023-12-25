class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       
    # Define the mapping of digits to letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        numbers = ['']
        for digit in digits:
            numbers = [old + new for old in numbers for new in phone_map[digit]]

        return numbers
