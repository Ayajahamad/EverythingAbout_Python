"""
We can change up to three elements in the array to minimize the amplitude. The four possible ways to do this are:

=> Remove the 3 largest values = New amplitude = amplitude1
amplitude1=arr[n−4]−arr[0]

=> Remove 2 largest + 1 smallest = New amplitude = amplitude2
amplitude2=arr[n−3]−arr[1]

=> Remove 1 largest + 2 smallest = New amplitude = amplitude3
amplitude3=arr[n−2]−arr[2]

=> Remove 3 smallest values = New amplitude = amplitude4
amplitude4=arr[n−1]−arr[3]

=> Finally, we take the minimum of these four computed amplitudes.
final amplitude=min(amplitude1,amplitude2,amplitude3,amplitude4)
"""

print("Hello..!")