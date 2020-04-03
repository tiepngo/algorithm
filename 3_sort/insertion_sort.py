import time
import random 
class InsertionSort:
    def __init__(self, arr):
        self.N =  len(arr)
        self.arr = arr
        self.min = 0
        self.t = time.time()
        # for i in range(self.N):
        #     for  j in range(i, -1,-1): 
        #         if self.arr[j] < self.arr[j-1]:
        #             self.exch(self.arr,j-1,j)
        #         else :
        #             break
        # 

        # Traverse through 1 to len(arr) 
        for i in range(1, self.N): 
    
            key = self.arr[i] 
            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = i-1
            while j >=0 and key < self.arr[j] : 
                    self.arr[j+1] = self.arr[j] 
                    j -= 1
            self.arr[j+1] = key 
        
        self.t = time.time() - self.t 
    def exch(self, arr, i,j ):
        ''' Exchange location i and j in array arr'''
        arr[i], arr[j] = arr[j], arr[i]

    def get_sorted(self):
        return self.arr 

    def get_time(self):
        return self.t 

