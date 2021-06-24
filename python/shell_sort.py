# Python3 program for implementation of Shell Sort

def shellSort(arr):
	gap = len(arr) // 2 # intiliaze the gap

	while gap > 0:
		i = 0
		j = gap
		
		# check the array in from left to right
		# till the last possible index of j
		while j < len(arr):
	
			if arr[i] >arr[j]:
				arr[i],arr[j] = arr[j],arr[i]
			
			i += 1
			j += 1
		
		# now we cannot move towards left anymore so
		# check the element from last index of i towards to left side of the array
		while i - gap != -1:

			if arr[i - gap] > arr[i]:
				arr[i-gap],arr[i] = arr[i],arr[i-gap]
			i -= 1

		gap //= 2


# driver to check the code
arr2 = [9,8,3,7,5,6,4,1]
print("input array:",arr2)

shellSort(arr2)
print("sorted array",arr2)

# This code is contributed by Shubham Prashar (SirPrashar)
