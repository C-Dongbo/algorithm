def quick_sorting(data:list):
    low, high = 0, len(data)-1
    def sort(low, high, data):
        if low >= high:
            return data
        pivot = partition(low, high)
        data = sort(low, pivot -1, data)
        data = sort(pivot, high, data)
        return data
    
    def partition(low, high):
        pivot = data[(low+high)//2]
        while low <= high:
            while data[low] < pivot:
                low+=1
            while data[high] > pivot:
                high-=1
            if low <= high:
                data[low], data[high] = data[high], data[low]
                low += 1
                high -= 1
        return low

    return sort(low, high, data)
if __name__=='__main__':
    test = [5,4,1,8,6,4,9,6,10]
    print(quick_sorting(test))