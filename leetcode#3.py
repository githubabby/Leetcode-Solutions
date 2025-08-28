# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# solution approach
# we can start ith brute force approach where we can check for all the substrings.
# we can optimise it using a sliding window approach. linear O(n) time complexity.
# we can use a set to keep track of characters.

'''
I initially though of keeping a dictinary to keep track of characters and their indices.
But a tutorial was using a set and I liked it more.'''

def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    maxlen = 0
    charSet = set()
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        maxlen = max(maxlen, r-l+1)
    return maxlen


def run_test_cases():
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0)
    ]
    for s, expected in cases:
        assert lengthOfLongestSubstring(s) == expected



def main():
    run_test_cases()
    print("All test cases passed.")

if __name__ == "__main__":
    main()