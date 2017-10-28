"""
Insertion Sort Algorithm v. 1.0
Coded by Kuba Siekierzyński (c) 2017
Original code:
https://code.sololearn.com/cgICdtdr5osG/#py

The code presents insertion sort algorithm in action. It is for educative purpose, contains comments and extensive printing.
It was prepared to answer a thread in he Q&A by Randiel Melgarejo:
https://www.sololearn.com/Discuss/403036/?ref=app

"""

def InsertionSortAlgorithm(lista):
    step = 0
    # we'll be counting algorithm iterations
    
    for i in range(1, len(lista)):
    # iterates through the list's elements
        
        j = i
        c = lista[i]
        # j assumes the default position of the sorted element
        # c assumes the current value of the sorted element
        
        while j > 0 and lista[j - 1] > c:
        # j has to be positive and the next element to the left greater than the currently sorted one
            
            lista[j] = lista[j - 1]
            # sorted element switches places with the one on the left
            
            j -= 1
            # again we check it with the one on its left
        
        lista[j] = c
        # the while loop ends if we hit a smaller element on he left, we insert the sorted element there and go back to the main for loop
        
        step += 1
        # another step is taken
        
        print(lista, '<-- step', step)
        # so let's print it out

list1 = [9, 4, 6, 3, 7, 1, 2, 8, 5]
print(list1, '<== input')
# prints the input list

InsertionSortAlgorithm(list1)
print(list1, '<== sorted')
# prints the input list, sorted
