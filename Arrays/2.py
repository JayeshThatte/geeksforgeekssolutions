# Question by : rithika palaniswamy : https://auth.geeksforgeeks.org/user/rithika%20palaniswamy
""" 
Program to find the minimum (or maximum) element of an array

Examples :

Input : arr[] = {1,2,3,-5}
Output :
Maximum : 3
Minimum : -5

Input : arr[] = {18,22,33,-25,0}
Output :
Maximum : 33
Minimum : -25

"""

# Function to find maximum
def maxi(array):

    #Set default value for maximum
    maxim = array[0]

    for i in range(len(array)):

        # If we get a value higher than maxim , update maxim
        if array[i] > maxim :
            maxim = array[i]
    return maxim

# Function to find minimum
def mini(array):

    #Set default value for minimum
    minim = array[0]

    for i in range(len(array)):

        # If we get a value lower than minim , update minim
        if array[i] < minim :
            minim = array[i]
    return minim


if __name__ == "__main__":

    arr = [1,2,3,-5]
    
    print("The maximum number is := ",maxi(arr))
    print("The minimum number is := ",mini(arr))