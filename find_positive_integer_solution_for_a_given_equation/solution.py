"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x+y

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int):
        cf = CustomFunction()
        
        result_list = []
        low = 1
        high = 1000
        while(low<=1000 and high>=1):
            if cf.f(low, high) > z:
                high -= 1
            elif cf.f(low,high) < z:
                low += 1
            else:
                result_list.append([low,high])
                low+=1
                high-=1
        return result_list


if __name__=='__main__':
    solution = Solution()
    print(solution.findSolution(CustomFunction,5))