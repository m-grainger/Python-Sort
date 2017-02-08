lst_1 = [67, 45, 2, 13, 1, 998]
lst_2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]

#insertion sort

def ins_sort(x,y):
    for index in range(1,len(x)): #starts us at the second to the left element in the list
        value = x[index] #value of element at that index
        i = index - 1 #compares values to the left
        while i>=0 and (value < x[i]): #stops when i gets to the beginning of the list AND the value is less than the i element in the list
            x[i+1] = x[i] #shift number in slot i right to slot i + 1
            x[i] = value #shift value to the left
            i = i - 1 #decrement i
        for index in range(1,len(y)):
            value = y[index]
            i = index - 1
            while i>=0 and (value < y[i]):
                y[i+1] = y[i]
                y[i] = value
                i = i - 1
                
ins_sort(lst_1, lst_2)
print(lst_1, lst_2)
           


