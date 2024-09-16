def swap(a, i, j):
    # This function swaps the elements at indices i and j in the list a.
    a[i], a[j] = a[j], a[i]  # Swap the values at positions i and j.

def sort_three(a):
    # This function sorts the first, middle, and last elements of the list a.
    n = len(a) - 1  # Get the index of the last element in the list.
    mid = n // 2    # Calculate the index of the middle element.

    # Check if the middle element is less than the first element.
    # If true, swap the first and middle elements to ensure the first is smaller.
    if a[mid] < a[0]:
        swap(a, 0, mid)  # Swap the elements at indices 0 and mid.

    # Check if the last element is less than the first element.
    # If true, swap the first and last elements to ensure the first is still the smallest.
    if a[n] < a[0]:
        swap(a, 0, n)  # Swap the elements at indices 0 and n.

    # Check if the last element is less than the middle element.
    # If true, swap the middle and last elements to ensure the middle element is not greater than the last.
    if a[n] < a[mid]:
        swap(a, mid, n)  # Swap the elements at indices mid and n.

# Test the function with a specific test case.
test_case = [2, 4, 1, 3, 5]  # Define a test case list.
sort_three(test_case)        # Call the sort_three function on the test case.
print(test_case)             # Print the modified test case to observe the result.
