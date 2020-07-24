@profile
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

@profile
def quick_sorting2(data :list):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in data:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sorting2(lesser_arr) + equal_arr + quick_sorting2(greater_arr)    


@profile
def TEST():

    test = [5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10,5,4,1,8,6,4,9,6,10]
    result = quick_sorting(test)
    result2 = quick_sorting2(test)
 
    print(result, result2)
 
if __name__ == "__main__":
    TEST()

