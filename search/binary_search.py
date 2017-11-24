"""
binary search

recursively partitions the list until the  key is found

time complexity: O(logn)
"""

def search(seq, key):
    """
    take a list of integers and searches if the key is contained within the list

    :param seq: a list of integers
    :param key: the integer to be searched for
    :return: the index of where the key is located in the list , if the key
    is not found then False is returned
    """

    low = 0
    high = len(seq) - 1

    while high > low:
        mid = low + (high - low)//2
        if seq[mid] < key:
            low += 1
        elif seq[mid] > key:
            high -= 1
        else:
            return mid
    return False


seq = [23,5,6,2,4,6,8,1,8,9,22,45,12,25,52,62]
seq = sorted(seq)
print (seq)
print (search(seq, 4))
