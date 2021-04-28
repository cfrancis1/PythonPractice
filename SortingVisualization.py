import random
import time
from pprint import pprint
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#BubbleSort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        sorted = True
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                temp1 = array[j]
                temp2 = array[j+1]
                array[j] = temp2
                array[j+1] = temp1
                sorted = False
                yield array
        if sorted:
            break

#InsertionSort
def insertion_sort(array):
    for i in range(1, len(array)):
        main_val = array[i]
        j = i -1
        while j >= 0 and array[j] > main_val:
            array[j + 1] = array[j]
            j = j - 1
            yield array
        array[j + 1] = main_val

#Merge Sort
def merge_sort(array):
    if len(array) > 1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)
        a = b = c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                array[c] = left[a]
                a += 1
            else:
                array[c] = right[b]
                b += 1
            c += 1
        while b < len(right):
            array[c] = right[b]
            b += 1
            c += 1
        while a < len(left):
            array[c] = left[a]
            a += 1
            c += 1
            
#Quick Sort
def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[randint(0, len(array) - 1)]
    low = []
    high = []
    equal = []
    for i in array:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        elif i == pivot:
            equal.append(i)
    return quick_sort(low) + equal + quick_sort(high)

#Init list
randomList = []

#Ask user for input
try:
    i = int(input("Enter any amount of values to sort (WARNING: More values means longer sorting time): "))
except ValueError:
    print("Not an integer value") #catch error

#Put random values into list randomly
for i in range(0,i):
    n = random.randint(0,250)
    randomList.append(n)

#Show the msurrent array to show it will be chnaged
print("This is your current array: ")
pprint(randomList)

#Ask them the sorting method they want to use
try:
    p = int(input("How would you like to sort your array?\n1. Bubble Sort, 2. Insertion Sort, 3. Merge Sort, 4. Quick Sort\n"))
except ValueError:
    print("Just enter the number, nothing else")

#Implement the sorting method they select
if p == 1:
    pprint(bubble_sort(randomList))
    title = "Bubble Sort"
    graph = bubble_sort(randomList)
elif p == 2:
    #pprint(insertion_sort(randomList))
    title = "Insertion Sort"
    graph = insertion_sort(randomList)
elif p == 3:
    #pprint(merge_sort(randomList))
    title = "Merge Sort"
    graph = merge_sort(randomList)
elif p == 4:
    #pprint(quick_sort(randomList))
    title = "Quick Sort"
    graph = quick_sort(randomList)

visual, axis = plt.subplots()
axis.set_title(title)
    
create_graph = axis.bar(range(len(randomList)), randomList, align="edge")
    
axis.set_xlim(0, i)
axis.set_ylim(0, 250)

loop =[0]

def visual_update(i, bars, loop):
	loop[0] += 1
	for bar, val in zip(bars, randomList):
   		bar.set_height(val)
visual = animation.FuncAnimation(visual, func=visual_update, fargs=(create_graph, loop), 
	frames = graph, interval = 1, repeat = False)
plt.show()