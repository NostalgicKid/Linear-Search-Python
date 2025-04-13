array = [1,2,4,56,54,2234,7564,32,9]
n = int(input("N: "))
def linear_search(arr, n):
    for x in arr:
        if x == n:
            return f"We found the number {n} in the array!"
    return f"We didn't find the number {n} in the array..."
print(linear_search(array, n))
