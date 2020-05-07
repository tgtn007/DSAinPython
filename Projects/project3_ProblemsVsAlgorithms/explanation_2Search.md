# Find the floored square root of the number
## Approach
I used binary search operation to find the pivot in which the array is rotated, after that we can divide the array into
two parts in which both is sorted, then I found in which part the target would lie and used regular binary search to
find the target element.

## Time Complexity 
My approach takes O(LogN) time as it is dividing the search into half each time.

## Space Complexity 
My approach is taking O(1) space complexity as we are not storing any lists or using any data structure.
 