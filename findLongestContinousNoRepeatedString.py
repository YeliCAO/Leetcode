def length_of_longest_substring(s):   
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        # Check if the current character has been used
        if s[i] in usedChar:
            # Slide window start to the right if the character is within our current window
            start = max(start, usedChar[s[i]] + 1)

        # Update the last seen index of the current character
        usedChar[s[i]] = i
        
        # Update max length if needed
        maxLength = max(maxLength, i - start + 1)
        print("Right now, the maxLength is: "+ str(maxLength))
        
    print("Finally maxLength:" + str(maxLength))
    return maxLength

def length_of_longest_substringV2(string):
    """
    Finds the length of the longest substring of s without repeating characters using a brute-force approach.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the longest substring.
    """
    length = len(string)
    longest = 0
    
    for i in range(length):
        current_chars = set()
        for j in range(i, length):
            if string[j] in current_chars:
                break
            else:
                current_chars.add(string[j])
                longest = max(longest, len(current_chars))
    print("Longest: "+str(longest))

    return longest


s="abcdefghijk"
length_of_longest_substringV2(s);
