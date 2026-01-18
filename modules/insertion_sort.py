def insertion_sort(arr):
    """Insertion sort that tracks steps for visualization"""
    n = len(arr)
    a = arr.copy()
    steps = []
    comparisons = [0]
    swaps = [0]
    
    for i in range(1, n):
        key = a[i]
        j = i - 1
        
        # Record initial state
        steps.append({
            'arr': a.copy(),
            'active': [i],
            'comparisons': comparisons[0],
            'swaps': swaps[0]
        })
        
        while j >= 0 and a[j] > key:
            comparisons[0] += 1
            
            # Record comparison step
            steps.append({
                'arr': a.copy(),
                'active': [j, j + 1],
                'comparisons': comparisons[0],
                'swaps': swaps[0]
            })
            
            a[j + 1] = a[j]
            swaps[0] += 1
            j -= 1
            
            # Record shift step
            steps.append({
                'arr': a.copy(),
                'active': [j + 1],
                'comparisons': comparisons[0],
                'swaps': swaps[0]
            })
        
        a[j + 1] = key
        swaps[0] += 1
        
        # Record insertion step
        steps.append({
            'arr': a.copy(),
            'active': [j + 1],
            'comparisons': comparisons[0],
            'swaps': swaps[0]
        })
    
    return steps if steps else [{'arr': a, 'active': [], 'comparisons': 0, 'swaps': 0}]
