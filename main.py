class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    if str(x) == ''.join(reversed(str(x))):
        return True

    return False

my = Solution()
n = 121
trueAns = True
ans = my.isPalindrome(n)
print("ans", ans, ans == trueAns)

# Runtime: 64 ms, faster than 73.40% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.6 MB, less than 95.38% of Python3 online submissions for Palindrome Number.