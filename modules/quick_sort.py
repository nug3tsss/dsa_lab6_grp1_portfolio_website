class QuickSort:
    def __init__(self, array):
        self.array = array
        self.sorted_array = self.quick_sort(self.array)

    def quick_sort(self, array):
        length = len(array)

        if length <= 1:
            return array
        
        pivot = array[-1]

        more = []
        less = []

        for item in array[:-1]:
            if item > pivot:
                more.append(item)

            else:
                less.append(item)

        return self.quick_sort(less) + [pivot] + self.quick_sort(more)
