class Solution:
    def peakIndexInMountainArray(self, A:list):
        return A.index(max(A))

    def peakIndexInMountainArray2(self, A:list):
        low = 0 
        high = len(A)-1
        while low < high:
            mid = int((low + high)/2)
            if A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low



if __name__ =='__main__':
    test = [0,2,1,0]
    solution = Solution()
    print(solution.peakIndexInMountainArray2(test))

        