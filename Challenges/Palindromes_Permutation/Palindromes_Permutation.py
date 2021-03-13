'''
Palindrome is a word or phrase that is the
same forwards and backwards

Palindrome Permutation: Given a string,
write a function to check if it is a 
permutation of a palindrome (Has no more than 1 odd letter). 

A permutation is a rearrangement of
letters. The palindrome does not need
to be limited to just dictionary words.
'''

#import collections
class Solution():
    # To Check if the word can be a Palindrome or Not (If have more than 1 odd letter then it cant be palindrome)
    def canPermutePalindrome(self, s):
        s = s.lower().replace(' ','') # convert to lower case and Replace spaces ' ' with no spaces ''

        # WITHOUT LIBRARY
        letter_ctr = {} # To store letter count
        odd_ctr = 0
        # Loop to count the letter
        for letter in s:
            # If already has the letter, then increment it
            if letter in letter_ctr:
                letter_ctr[letter] += 1
            # If not, then add it
            else:
                letter_ctr[letter] = 1

        # WITH LIBRARY 'collections'
        #letter_ctr = collections.Counter(s)
        

        for letter in letter_ctr:
            # If not 0 (odd) then go to this statement
            if letter_ctr[letter] % 2 != 0:
                odd_ctr += 1
        return odd_ctr <= 1
    
    # To Check if current word is Palindrome or Not
    def is_itPalindrome(self, s):
        s = s.lower().replace(' ','')
        return s == s[::-1] # Check forwards and backwards if it reads the same

check = Solution()
# Can it be a Palindrome?
print(check.canPermutePalindrome('saasr'))

# Is it Palindrome?
print(check.is_itPalindrome('nurses run'))