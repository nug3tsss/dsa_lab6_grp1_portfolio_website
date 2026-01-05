class MergeSort():
    def __init__(self, array):
        self.array = array
        self.merge_sort(self.array)
    
    def merge_sort(self, array):
        array_length = len(array)

        if array_length <= 1:
            # Stop recursion
            return array
        
        middle_array = array_length // 2
        left_array = array[:middle_array]
        right_array = array[middle_array:]
        
        self.merge_sort(left_array)
        self.merge_sort(right_array)
        self.merge(left_array, right_array, array)

    def merge(self, left_array, right_array, array):
        left_size = len(left_array)
        right_size = len(right_array)

        # Indices
        i = 0
        l = 0
        r = 0

        while l < left_size and r < right_size:
            if left_array[l] < right_array[r]:
                array[i] = left_array[l]
                i += 1
                l += 1
            else:
                array[i] = right_array[r]
                i += 1
                r += 1
        
        while l < left_size:
            array[i] = left_array[l]
            i += 1
            l += 1
        
        while r < right_size:
            array[i] = right_array[r]
            i += 1
            r += 1

array = [1, 7, 3, 6, 2, 8]
MergeSort(array)
print(array)
