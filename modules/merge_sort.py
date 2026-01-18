def merge_sort(array):
    """Merge sort that tracks steps for visualization"""
    n = len(array)
    a = array.copy()
    steps = []
    comparisons = [0]
    swaps = [0]
    
    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)
    
    def merge(arr, left, mid, right):
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            comparisons[0] += 1
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            
            swaps[0] += 1
            k += 1
            
            steps.append({
                'arr': arr.copy(),
                'active': [k-1],
                'comparisons': comparisons[0],
                'swaps': swaps[0]
            })
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            swaps[0] += 1
            
            steps.append({
                'arr': arr.copy(),
                'active': [k-1],
                'comparisons': comparisons[0],
                'swaps': swaps[0]
            })
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            swaps[0] += 1
            
            steps.append({
                'arr': arr.copy(),
                'active': [k-1],
                'comparisons': comparisons[0],
                'swaps': swaps[0]
            })
    
    merge_sort_helper(a, 0, n - 1)
    return steps if steps else [{'arr': a, 'active': [], 'comparisons': 0, 'swaps': 0}]
