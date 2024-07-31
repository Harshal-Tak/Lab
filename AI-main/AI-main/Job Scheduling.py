def printJobScheduling(arr, t):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
    # To keep track of free time slots
    result = [False] * t
 
    # To store result (Sequence of jobs)
    job = ['-1'] * t
 
    # Iterate through all given jobs
    for i in range(len(arr)):
 
        # Find a free slot for this job
        # (Note that we start from the
        # last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
 
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
 
    # print the sequence
    print(job)

arr = [[1, 2, 50], [2, 1, 10], [3, 3, 40], [4, 2, 60], [5, 1, 30], [6, 3, 20]]
 
print("Following is maximum profit sequence of jobs")
 
    
printJobScheduling(arr, 3)
