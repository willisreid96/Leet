class Solution(object):
    #Initialize a dictionary char_dict to keep track of characters and their last seen indices.
        #Initialize variables max_length and start to keep track of the maximum length and the start of the current substring.
        #Iterate through the characters in the string using a loop with end as the iterator.
        #If the character at end is already in char_dict and its last seen index is greater than or equal to start, update start to be one more than the last seen index of the character.
        #Update the last seen index of the character in char_dict.
        #Update max_length to be the maximum of the current max_length and the length of the current substring (end - start + 1).
        #Return max_length after the loop.
    def lengthOfLongestSubstring(self, s):
        
        # Initialize a dictionary to keep track of characters and their indices
        char_dict = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_dict and char_dict[s[end]] >= start:
                start = char_dict[s[end]] + 1
            char_dict[s[end]] = end
            max_length =max(max_length, end - start + 1)
        return max_length
    
