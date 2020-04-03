import time
import random 
class QuickSort:
    def __init__(self, arr):
        self.N =  len(arr)
        self.arr = arr
        self.min = 0
        self.t = time.time()
        random.shuffle(self.arr)
        self.sort(self.arr,0,self.N -1)
        
        self.t = time.time() - self.t 
    
    def sort(self,arr, lo, hi):
        if hi <= lo:
            return
        k = self.partition(arr, lo, hi)
        self.sort(arr,lo ,k-1)
        self.sort(arr,k+1, hi )

    def partition(self, xs, start, end):
        follower = leader = start
        while leader < end:
            if xs[leader] <= xs[end]:
                xs[follower], xs[leader] = xs[leader], xs[follower]
                follower += 1
            leader += 1
        xs[follower], xs[end] = xs[end], xs[follower]
        return follower


    def exch(self, arr, i,j ):
        ''' Exchange location i and j in array arr'''
        arr[i], arr[j] = arr[j], arr[i]

    def get_sorted(self):
        return self.arr 

    def get_time(self):
        return self.t 

if __name__ == "__main__":
    _qs = QuickSort([2, 4, 0, 1, 3, 3, 4, 0, 1 ,2,1000])
    print(_qs.get_sorted())
