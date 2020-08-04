class Solution:
    def minDistance(self, word1: str, word2: str):
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)

        if len(word2) == 0:
            return len(word1)

        previous_row = range(len(word2) + 1)
        for i, c1 in enumerate(word1):
            current_row = [i + 1]
            for j, c2 in enumerate(word2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                replace = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, replace))

            previous_row = current_row

        return previous_row[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance('horse','ros'))