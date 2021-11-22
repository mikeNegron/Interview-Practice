#Problem:
#Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    '''
    Sliding window needs: a [window], [left ptr], [right ptr] and an [output]
    POSSIBLE CASES:
    Base Case: If not found, increase the size of the curr. window to the right
    Case 1: If dupe is found, move left ptr to [right - 1] idx and eval. length
    Case 2: If char is found before curr. char, increase new window to the right
       
    Time Complexity = O(n)
    Space Complexity = O(m)
    '''
    if not s: return 0

    window = {}
    left = 0
    output = 1
    
    for right, val in enumerate(s):
        if val not in window: #Base Case
          output = max(output, right - left + 1)
                
        else:
            if window[val] < left: #Case 2
                output = max(output, right - left + 1)
            else: #Case 1
                left = window[val] + 1
                    
        window[val] = right 
    return output

def main():
    #The longest substring would be 'wke'. Remember that substrings are contiguous-ish
    test = 'pwwkew' 

    result = lengthOfLongestSubstring(test)

    print(f'The length of longest SubString is: {result}')

if __name__ == '__main__':
    main()
        