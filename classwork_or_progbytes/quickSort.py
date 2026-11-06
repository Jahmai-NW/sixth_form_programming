def quick_sort(items, start, end):
    
    # Base case for recursion:
    # The recursion will stop when the partition contains a single item
    if start >= end:
        return

    # Otherwise recursively call the function
    else:
        pivot_value = items[start] # Set to first item in the partition
        low_mark = start + 1 # Set to second position in the partition
        high_mark = end # Set to last position in the partition
        finished = False
        
        # Repeat until low and high values have been swapped as needed
        while finished == False:
            
            # Move the left pivot
            while low_mark <= high_mark and items[low_mark] <= pivot_value:
                low_mark = low_mark + 1 # Increment low_mark
                
             # Move the right pivot                               
            while items[high_mark] >= pivot_value and high_mark >= low_mark:
                high_mark = high_mark - 1 # Decrement high_mark

            # Check that the low mark doesn't overlap with the high mark
            if low_mark < high_mark:
                # Swap the values at low_mark and high_mark
                temp = items[low_mark]
                items[low_mark] = items[high_mark]
                items[high_mark] = temp
                
            # Otherwise end the loop
            else:
                finished = True
            
        # Swap the pivot value and the value at high_mark
        temp = items[start]
        items[start] = items[high_mark]
        items[high_mark] = temp
   
        # Recursive call on the left partition
        quick_sort(items, start, high_mark - 1)

        # Recursive call on the right partition
        quick_sort(items, high_mark + 1, end)
    return items


leAura = [6, 49, 15, 8, 5, 13, 24, 55]
print     (quick_sort(leAura, 0, 7))
