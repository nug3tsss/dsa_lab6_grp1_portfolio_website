def quick_sort(arr):
    """Quick sort that tracks steps for visualization"""
    n = len(arr)
    a = arr.copy()
    steps = []
    comparisons = [0]
    swaps = [0]
    
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparisons[0] += 1
            
            # Record comparison step
            steps.append({
                'arr': arr.copy(),
                'active': [j, high],
                'comparisons': comparisons[0],
                'swaps': swaps[0]
            })
            
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
                
                # Record swap step
                steps.append({
                    'arr': arr.copy(),
                    'active': [i, j],
                    'comparisons': comparisons[0],
                    'swaps': swaps[0]
                })
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
        
        # Record final swap step
        steps.append({
            'arr': arr.copy(),
            'active': [i + 1, high],
            'comparisons': comparisons[0],
            'swaps': swaps[0]
        })
        
        return i + 1
    
    quick_sort_helper(a, 0, n - 1)
    return steps if steps else [{'arr': a, 'active': [], 'comparisons': 0, 'swaps': 0}]
