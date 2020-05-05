# Union and Intersection

## Data Structure 
We use sets in this problem, as it contains only unique values and we are dealing with unique values for intersection
and union of linkedlists.

## Time Complexity
Union : It will take O(N) time complexity to iterate and add the items in set.

Intersection : It will take worst case complexity of O(N^2) as there is a search within loop which will iterate though
the list for each item.

## Space Complexity
It will take o(N) space complexity to store all the elements in set, more precisely if all the elements of both linked 
list are different, then it will take space equal to sum of number of elements of both linked list.