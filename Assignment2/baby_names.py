import re

# Read the HTML file
file_path = 'baby2008.html'
with open(file_path, 'r') as f:
    contents = f.read()

# Use regex to extract names
def find_names(html):
    pattern = re.compile(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>')
    matches = pattern.findall(html)
    return matches

# Extract names
names = find_names(contents)
male_names = [name[1] for name in names]
female_names = [name[2] for name in names]

# Sorting algorithm (bubble sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Binary search algorithm
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Sort the names
sorted_male_names = bubble_sort(male_names)
sorted_female_names = bubble_sort(female_names)
print(f"Extracted male names is {len(male_names)}")
print(f"Extracted female names is {len(female_names)}")

# Print sorted names
print("Sorted Male Names:", sorted_male_names)
print("Sorted Female Names:", sorted_female_names)

# Search for a name
name_to_search = "Jacob"
male_index = binary_search(sorted_male_names, name_to_search)
female_index = binary_search(sorted_female_names, name_to_search)

if male_index != -1:
    print(f"Male name '{name_to_search}' found at index {male_index}")
else:
    print(f"Male name '{name_to_search}' not found")

if female_index != -1:
    print(f"Female name '{name_to_search}' found at index {female_index}")
else:
    print(f"Female name '{name_to_search}' not found")