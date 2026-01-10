class SelectionSort:
    def __init__(self, array):
        self.array = array
        self.selection_sort(self.array)

    def selection_sort(self, array):
        n = len(array)

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if array[j] < array[min_index]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]

        return array
