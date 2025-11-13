def merge_sort(arr):
    if len(arr) <= 1:  # Base case: array of 0 or 1 element is sorted
        return arr
    
    mid = len(arr) // 2  # Find the midpoint to divide the array
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Merge the two sorted halves into one sorted array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Append remaining elements (if any) from left or right
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Example usage:
arr = [8, 1, 3, 2, 1, 5, 3, 7, 9]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
