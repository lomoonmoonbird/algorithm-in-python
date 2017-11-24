
def binary_search(array, value):
    print '@@'
    low = 0
    high = len(array) - 1
    while low <high:

        mid = (low + high)/2
        print low,mid, high
        if array[mid] > value:
            high = mid
        elif array[mid] < value:
            low = mid + 1
        else: return mid
    return low if array[low] == value else False

print binary_search([1,2,3,4,5,6], 3), '###'