# Regular_Expression_Matching

Can you solve this real interview question? Regular Expression Matching - Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

 * '.' Matches any single character.
 * '*' Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

 

Example 1:


Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".


Example 2:


Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".


Example 3:


Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


 

Constraints:

 * 1 <= s.length <= 20
 * 1 <= p.length <= 20
 * s contains only lowercase English letters.
 * p contains only lowercase English letters, '.', and '*'.
 * It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

---

## Metadata

- Language: python3
- Difficulty: Unknown
- Acceptance: 96.03
- Tags: 
- URL: https://leetcode.com/problems/regular-expression-matching/submissions/2185341075/

## Files

- Regular_Expression_Matching.py
