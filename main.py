def longestIncreasingSub(arr):
    longest = 0
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr) and arr[j] > arr[j - 1]:
            j += 1
        longest = max(longest, j - i)
    
    return longest


if __name__ == "__main__":
    a = [1, 3, 5, 4, 7]
    b = [1, 3, 5, 7, 4, 1, 2, 3, 4, 5, 7, 8, 9]
    c = [2, 2, 2, 2]
    print(longestIncreasingSub(a))
    print(longestIncreasingSub(b))
    print(longestIncreasingSub(c))
