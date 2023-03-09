def swap(arr, i):
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp

n = 9
nuts = ['^', '&', '%', '@', '#', '*', '$', '~', '!']
bolts = ['~', '#', '@', '%', '&', '*', '$', '^', '!']
bFlag = True

while bFlag:
    count = 0
    for i in range(n-1):
        if (nuts[i] == bolts[i]):
            if (nuts[i+1] > bolts[i] and count >= n-2):
                bFlag = False
                break
            elif (nuts[i+1] > bolts[i]):
                count += 1
                continue
            else:
                swap(nuts, i)
                swap(bolts, i)               
        elif (nuts[i] > bolts[i]):
            swap(nuts, i)
        elif (nuts[i] < bolts[i]):
            swap(bolts, i)
    #Output
    for i in range(n):
        print(nuts[i], end=" ")
    print()
    for i in range(n):
        print(bolts[i], end=" ")
    print('\n')
input()

