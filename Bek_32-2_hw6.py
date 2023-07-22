def selection_sort(unsorted_list):
    l = len(unsorted_list)
    ind = 0

    while ind < l - 1:
        smallest = ind
        j = ind + 1

        while j < l:
            if unsorted_list[j] < unsorted_list[smallest]:
                smallest = j

            j+=1
        unsorted_list[ind], unsorted_list[smallest] = unsorted_list[smallest], unsorted_list[ind]
        print(unsorted_list)
        ind+=1

    return unsorted_list


lst = [100, 23, 45, 1, 21, 213, 7, 41, 25]




def binary_search(element_to_search, list):
    N = list
    first = 0
    last = len(N) - 1

    while first <= last:
        middle = (first + last) // 2
        if element_to_search == N[middle]:
            print('ID =', middle)
            break

        if element_to_search > N[middle]:
            first = middle + 1
        else:
            last = middle - 1
    else:
        print('NO VALUE')

sList = [1, 7, 21, 23, 25, 41, 45, 100, 213]

selection_sort(lst)
binary_search(21, sList)

