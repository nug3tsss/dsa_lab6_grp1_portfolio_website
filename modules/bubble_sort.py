def bubble_sort(arr):
    n = len(arr)
    a = arr.copy()
    steps = []
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1

            # Record comparison step
            steps.append({
                'arr': a.copy(),
                'active': [j, j + 1],
                'comparisons': comparisons,
                'swaps': swaps,
                'swapped': False
            })

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

                # Record swap step
                steps.append({
                    'arr': a.copy(),
                    'active': [j, j + 1],
                    'comparisons': comparisons,
                    'swaps': swaps,
                    'swapped': True
                })

    return steps