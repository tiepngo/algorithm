from insertion_sort  import InsertionSort
from selection_sort  import SelectionSort
from merge_sort      import MergeSort
import random

test_list = [2, 4, 0, 1, 3, 3, 4, 0, 1 ,2,1000]
def test_sort():
    _is = InsertionSort(test_list)
    _ss = SelectionSort(test_list)
    _ms = MergeSort(test_list)

    assert _is.get_sorted() == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 1000]
    assert _ss.get_sorted() == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 1000]
    assert _ms.get_sorted() == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 1000]

for i in [2**i for i in range(10,15)] :
    l = list(range(i))
    random.shuffle(l)
    _is = InsertionSort(l)
    _ss = SelectionSort(l)
    _ms = MergeSort(l)
    print("N = {} , SelectionSort {}s , InsertionSort {}s, MergeSort {}s ".format(i,_ss.get_time(),_is.get_time(), _ms.get_time()))

    #print(s.get_sorted())