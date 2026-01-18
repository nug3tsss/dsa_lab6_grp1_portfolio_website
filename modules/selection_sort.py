def selection_sort(arr):
    """Selection sort that tracks steps for visualization"""
    n = len(arr)
    a = arr.copy()
    steps = []
    comparisons = [0]
    swaps = [0]

    for i in range(n):
        min_index = i

        # Record initial state for this pass
        steps.append(
            {
                "arr": a.copy(),
                "active": [i],
                "comparisons": comparisons[0],
                "swaps": swaps[0],
            }
        )

        for j in range(i + 1, n):
            comparisons[0] += 1

            # Record comparison step
            steps.append(
                {
                    "arr": a.copy(),
                    "active": [min_index, j],
                    "comparisons": comparisons[0],
                    "swaps": swaps[0],
                }
            )

            if a[j] < a[min_index]:
                min_index = j

        # Swap if needed
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps[0] += 1

            # Record swap step
            steps.append(
                {
                    "arr": a.copy(),
                    "active": [i, min_index],
                    "comparisons": comparisons[0],
                    "swaps": swaps[0],
                }
            )

    return (
        steps
        if steps
        else [{"arr": a, "active": [], "comparisons": 0, "swaps": 0}]
    )
