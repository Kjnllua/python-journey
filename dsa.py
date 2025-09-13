# %%
# Question 1: Implement linear search in Python to find a target value in a list. Return the index if found, or None if not found.
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return None

if __name__ == "__main__":
    # Test cases will be run automatically
    print("Testing linear_search...")
    test_cases = [
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 6, None),
        ([], 5, None),
        ([10], 10, 0)
    ]
    
    for arr, target, expected in test_cases:
        result = linear_search(arr, target)
        print(f"linear_search({arr}, {target}) = {result}, expected {expected}")


# %%
# Question 2: Challenge: Implement binary search for a SORTED list in Python. Much faster than linear search for large datasets! 
def binary_search(arr, target):
    """
    Search for target in SORTED arr using binary search.
    
    Args:
        arr: SORTED list of integers to search
        target: Value to find
    
    Returns:
        Index of target if found, None otherwise
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == arr[mid]: 
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Test your function
if __name__ == "__main__":
    print("Testing binary_search...")
    test_cases = [
        ([1, 3, 5, 7, 9, 11], 7, 3),
        ([1, 3, 5, 7, 9, 11], 4, None),
        ([], 5, None),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4)
    ]
    
    for arr, target, expected in test_cases:
        result = binary_search(arr, target)
        print(f"binary_search({arr}, {target}) = {result}, expected {expected}")


# %%
# Question 3: Challenge: Implement bubble sort in Python to sort a list in ascending order. Compare adjacent elements and swap if they're in wrong order. 
def bubble_sort(arr):
    """
    Sort arr using bubble sort algorithm.
    
    Args:
        arr: List of integers to sort
    
    Returns:
        New sorted list (don't modify original)
    """
    # Create a copy to avoid modifying the original
    result = arr.copy()
    
    for i in range(len(result)):
        for j in range(0, len(result)-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result

# Test your function
if __name__ == "__main__":
    print("Testing bubble_sort...")
    test_cases = [
        [64, 34, 25, 12, 22],
        [5, 1, 4, 2, 8],
        [1],
        [],
        [3, 3, 3, 1, 2]
    ]
    
    for arr in test_cases:
        original = arr.copy()
        result = bubble_sort(arr)
        expected = sorted(arr)
        print(f"bubble_sort({original}) = {result}")
        print(f"Expected: {expected}, Correct: {result == expected}")
        print()
