"""
Given an array arr[] and size of array is n and one another key x, and give you a segment size k. The task is to find that the key x present in every segment of size k in arr[].
Examples: 

Input : 
arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3} 
x = 3 
k = 3 
Output : Yes 
There are 4 non-overlapping segments of size k in the array, {3, 5, 2}, {4, 9, 3}, {1, 7, 3} and {11, 12, 3}. 3 is present all segments.
Input : 
arr[] = { 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25} 
x = 23 
k = 5 
Output :Yes 
There are three segments and last segment is not full {21, 23, 56, 65, 34}, {54, 76, 32, 23, 45} and {21, 23, 25}. 
23 is present all window.
Input :arr[] = { 5, 8, 7, 12, 14, 3, 9} 
x = 8 
k = 2 
Output : No
"""


# Way 1

def split_segments(array:list, k:int) -> list:

    """ We split the given array into n smaller arrays of size <= k """

    segments = []
    pos = 0

    # If length of array is divisible by k , we get all arrays of same k
    # If not , we get unequal array. so we add 1  , to get 1 more mini array

    add = 0
    if len(array) % k != 0:
        add = 1

    for i in range(int(len(array) / k) + add):
        segments.append(array[pos:pos + k])
        pos += k

    return segments


def check_no1(array, x, k):

    """ We check if the x is present in segments generated after passing k. """

    segments = split_segments(array, k)
    final_ans = 'Available in all segments'

    for i in segments:

        # We check if x is in segment 
        if x in i :
            print(f'{x} present in {i}')
        if x not in i:
            final_ans = 'Not available in all segments'

    print(final_ans)


# Way 2

def check_no2(array, x, k):

    """ We use this function to check within the array , without making new array """

    startpos = 0
    endpos = k
    flag = present_all = True

    while flag:
        # If elem is in the current segment
        present_segment = False

        #Check for x in segment
        for i in range(startpos, endpos):

            #Break out of all loops if we hit end of array
            if i >= len(array):
                # Present all means x in all segments
                if present_all:
                    print('Available in all segments')
                else:
                    print('Not available in all segments')

                flag = False
                break

            if array[i] == x:
                present_segment = True
                print(f'{x} present in subarray {array[startpos:endpos]}')

                # If we find that element has occured , why check till end for more ?
                # So break out of sub array

                break

        # Set present all as current value and present in segment
        present_all = present_all and present_segment

        # update startpos and end pos
        startpos = endpos
        endpos += k


# Driver Code
if __name__ == "__main__":

    arr= [ 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3 ] 
    x = 3 
    k = 3 

    print('--------')
    print('Way 1')
    print('--------')

    check_no1(arr,x,k)

    print('--------')
    print('Way 2')
    print('--------')
    
    check_no2(arr,x,k)