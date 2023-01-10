def permute(arr, start):
    if start == len(arr):
        print(arr)
    else:
        for i in range (start, len(arr)):
            # Swap
            t = arr[start]
            arr[start] = arr[i]
            arr[i] = t
            permute(arr, start + 1)
            # Swap back
            t = arr[start]
            arr[start] = arr[i]
            arr[i] = t

permute(['a', 'b', 'c', 'd'], 0)