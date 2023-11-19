def find_unsorted_subarray(arr):

    start = 0
    while start < len(arr) - 1 and arr[start] <= arr[start + 1]:
        start += 1

    if start == len(arr) - 1:
        return [0, 0]

    end = len(arr) - 1
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    min_val = min(arr[start:end + 1])
    max_val = max(arr[start:end + 1])

    while start > 0 and arr[start - 1] > min_val:
        start -= 1
    while end < len(arr) - 1 and arr[end + 1] < max_val:
        end += 1

    return [start, end]
    

arr = [1, 2, 3, 6, 4, 4]
result = find_unsorted_subarray(arr)
print(result)
