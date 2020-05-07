#Rearrange Array Digits
## Approach
I used quick sort to sort the elements of digits then appended the one digit to each first and second number starting
from the end, which will yield max value.

## Time Complexity 
My approach takes O(N Log N) time complexity to sort the array by using quick sort, but it may go to 
O(N^2) if the array is already sorted.

## Space Complexity 
My approach is taking O(1) space complexity as we are not storing any lists or using any additional data structure.