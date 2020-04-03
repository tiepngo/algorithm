import time
import random 
class SelectionSort:
    def __init__(self, arr):
        self.N =  len(arr)
        self.arr = arr
        self.min = 0
        self.t = time.time()
        for i in range(self.N):
            self.min = i 
            for  j in range(i+1, self.N): 
                if self.arr[i] > self.arr[j]:
                    self.min = j
            self.exch(self.arr, i, self.min)
        self.t = time.time() - self.t 

    def exch(self, arr, i,j ):
        ''' Exchange location i and j in array arr'''
        arr[i], arr[j] = arr[j], arr[i]

    def get_sorted(self):
        return self.arr 

    def get_time(self):
        return self.t 


