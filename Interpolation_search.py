def interpolation_search(arr, lo, hi, x):
    if lo <= hi and x >= arr[lo] and x <= arr[hi]:
        pos = lo + ((x - arr[lo]) // (arr[hi] - arr[lo]) * (hi - lo))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, hi, x)
        if arr[pos] > x:
            return interpolation_search(arr, lo, pos - 1, x)
    return -1
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n = len(arr)
x = 18
index = interpolation_search(arr, 0, n - 1, x)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")