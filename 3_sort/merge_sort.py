import time
import random 
class MergeSort:
    def __init__(self, arr):
        self.N =  len(arr)
        self.arr = arr
        self.min = 0
        self.t = time.time()

        self.sort(arr, 0 , self.N -1 )
        
        self.t = time.time() - self.t 
    def sort(self, arr, lo ,hi) :
        mid = lo + (hi-lo)//2
        #print("Debug : {} {} {}".format(lo, mid, hi))
        if hi <= lo :
            return
        self.sort(arr,lo, mid)
        self.sort(arr, mid+1, hi)
        self.merge(arr,lo, mid, hi) 

    def merge(self, arr, lo, mid, hi):
        i = lo 
        j = mid + 1 
        self.aux  = arr.copy()

        for k in range(lo, hi+1):
            if i > mid :
                arr[k] = self.aux[j]
                j +=1
            elif j > hi :
                arr[k] = self.aux[i]
                i += 1
            elif self.aux[j] < self.aux[i]:
                arr[k] = self.aux[j]
                j += 1
            else :
                arr[k] = self.aux[i]
                i += 1


    def exch(self, arr, i,j ):
        ''' Exchange location i and j in array arr'''
        arr[i], arr[j] = arr[j], arr[i]

    def get_sorted(self):
        return self.arr 

    def get_time(self):
        return self.t 

if __name__ == '__main__' :
    test_list = [2, 4, 0, 1, 3, 3, 4, 0, 1 ,2,1000]
    _ms = MergeSort(test_list)

    def test_sort():
        assert _ms.get_sorted() == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 1000]