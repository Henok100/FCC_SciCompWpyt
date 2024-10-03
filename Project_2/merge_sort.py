# Title: Merge Sort Algorithm Implementation
# 
# Introduction:
# This script implements the Merge Sort algorithm, which is a popular sorting algorithm
# that uses the "divide-and-conquer" approach. The array is split into two halves, each half 
# is recursively sorted, and then the two sorted halves are merged back together.
# Merge Sort works efficiently on large datasets and has a time complexity of O(n log n).
# In this implementation, we'll explain each part of the process step by step.

def merge_sort(array):
    # Step 1: Base case for recursion
    # If the array has 1 or fewer elements, it's already sorted, so we just return.
    # This stops the recursion when the array can't be split further.
    if len(array) <= 1:
        return
    
    # Step 2: Find the middle point of the array to split it into two halves
    # The "middle_point" is calculated by dividing the length of the array by 2.
    middle_point = len(array) // 2
    
    # Step 3: Split the array into two sub-arrays
    # The array is divided into a "left_part" and a "right_part".
    # left_part will hold the first half of the array (from the start to the middle).
    # right_part will hold the second half (from the middle to the end).
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Step 4: Recursively sort both halves of the array
    # We recursively call merge_sort to sort each half separately.
    # First, the left part is sorted, then the right part.
    merge_sort(left_part)
    merge_sort(right_part)

    # Step 5: Initialize pointers for merging
    # We create three pointers:
    # - left_array_index for traversing the left_part.
    # - right_array_index for traversing the right_part.
    # - sorted_index for placing the sorted elements into the original array.
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Step 6: Merge the two sorted halves back into the original array
    # This is where the actual merging happens. We compare elements from both halves 
    # and copy the smaller one into the original array.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Compare the current elements of left_part and right_part.
        # If the element from left_part is smaller, place it in the array.
        if left_part[left_array_index] < right_part[right_array_index]:
            # Place the element from the left part into the array.
            array[sorted_index] = left_part[left_array_index]
            # Move the left_array_index pointer to the next element.
            left_array_index += 1
        else:
            # Otherwise, place the element from the right part into the array.
            array[sorted_index] = right_part[right_array_index]
            # Move the right_array_index pointer to the next element.
            right_array_index += 1
        # Move the sorted_index pointer to the next position in the array.
        sorted_index += 1

    # Step 7: Handle any remaining elements in the left_part
    # If there are any elements left in the left_part (after the above loop ends),
    # we copy them into the array.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Step 8: Handle any remaining elements in the right_part
    # If there are any elements left in the right_part, we copy them into the array.
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# This is the main block of the program that runs the merge_sort function on an example array.
# We use an "if __name__ == '__main__':" block to ensure that the code only runs
# if the script is executed directly, not imported as a module.
if __name__ == '__main__':
    # Step 9: Create an unsorted array of numbers for demonstration
    # This list will be sorted using the merge_sort function.
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    
    # Display the unsorted array before sorting.
    print('Unsorted array: ')
    print(numbers)
    
    # Step 10: Call the merge_sort function to sort the array
    # The merge_sort function will sort the "numbers" list in place.
    merge_sort(numbers)
    
    # Display the sorted array after the merge_sort function has run.
    print('Sorted array: ' + str(numbers))
