# Finding Files

## Data Structure 
We use the algorithm recursion to recursively go through all the directories inside the file to find the files with the 
desired suffix, we then append the path to a list. We may see it as a DFS search to go to each nodes and check.

## Time Complexity
The time complexity to find all the files is O(N) no of files it had to check in the given path's directory and all it's
subdirectories.

## Space Complexity
The worst case complexity will the linear that is number of directories to store it in recursion call stack.