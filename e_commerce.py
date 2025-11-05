

def linear_search(ids, target):
    return target in ids

def binary_search(ids, target):
    ids.sort()
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            return True
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Main program
customer_ids = [101, 104, 107, 109, 113, 120, 125, 130]
target = int(input("Enter Customer Account ID to search: "))


print("Linear Search:", "Found" if linear_search(customer_ids, target) else "Not Found")
print("Binary Search:", "Found" if binary_search(customer_ids, target) else "Not Found")

