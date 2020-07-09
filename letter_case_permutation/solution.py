class Solution:
    def letterCasePermutation(self, S):
        result = []
        def dfs(chars, i):
            if i == len(chars):
                result.append(''.join(chars))
            else:
                char = chars[i]
                if char.isalpha():
                    chars[i] = char.lower()
                    dfs(chars, i+1)
                    chars[i] = char.upper()
                    dfs(chars, i+1)
                else:
                    dfs(chars, i+1)
        chars = list(S)
        dfs(chars, 0)

        return result


if __name__ == '__main__':
    test = 'ABC123'
    solution = Solution()
    print(solution.letterCasePermutation(test))