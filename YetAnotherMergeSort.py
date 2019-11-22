def mergeSort(alist):
    print("Splittingdata ",alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

# copy data to temp lists
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i = i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

# checking to see if any item was left
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Mergingdata ", a_list)
def printList(a_list):
    for i in range(len(a_list)):
        print(a_list[i],end=" ")
    print()

#if the Python interpreter is running that module (the source file) as the main program,
#it sets the special __name__ variable to have a value "__main__".
#If this file is being imported from another module, __name__ will be set to the module's name


if __name__ == '__main__':
    a_list = [54,26,93,17,77,31,44,55,20]
    print ("Given array is", end="\n")
    printList(a_list)
    mergeSort(a_list)
    print("Sorted array is: ", end="\n")
    printList(a_list)

