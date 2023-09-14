def bubble_sort(u):
    n = len(u)
    swapped = False

    for i in range(n-1):
        for j in range(0,n - i - 1):
            if  u[j] > u[j + 1]:
                swapped = True
                u[j], u[j + 1] = u[j + 1], u[j]

            if not swapped:
                return 

u = [23, 1, 3, 50, 100, 45, 2]
print(u)    
bubble_sort(u)

print("Sorted array is: ")
for i in range(len(u)):
    print("% d" % u[i], end=" ") 

