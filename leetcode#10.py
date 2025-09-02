# 10. Regular Expression Matching
# Given an input string s and a pattern p, 
# implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


# so right now this is not working for 1 specific case that is * can match 0 for prev char.

def isMatch(self, s: str, p: str) -> bool:
    def helper(i, j):
        if i>=len(s) or j>=len(p):
            return False
        print(s[i],p[j])
        if p[j]==".":
            return helper(i,j+1) or helper(i+1,j+1) if i+1<len(s) or j+1<len(p) else True
        elif p[j]=="*":
            return helper(i,j+1) or helper(i+1,j+1) or helper(i+1,j) if i+1<len(s) or j+1<len(p) else True
        else:
            return helper(i+1,j+1) if s[i]==p[j] else False
            
    return helper(0,0)