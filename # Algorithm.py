# Operations with Data Structures
    1. Insert
    2. Delete
    3. Search
    4. Access


# Topic Wise Importance
    1. Concepts
        Big O Notations
        Memory
        Logarithm
        Recursion
    
    2. Data Structures
            A DS is way of organizing and holding data in some manner in an efficient way so that it can be accessed, queried or even updated easily and quickly.
        Array
        Linked List
        Stack
        Queue
        Hash Tables
        Trees
        Heaps
        Tries
        Graph


Array Example in C              # a collection of (self-indexed from 0) elements of the same data types are stored contiguous memory locations
----------------------------
#include <stdio.h>

int main()
{
    int arr[] = {1,2,3,4,5};
    printf("%d", arr[3]);
    return 0;
    }
----------------------------
        
        
        
    3. Algorithms           (performs over data structures)
        Sorting algorithm   a set of steps to search
        Searching           a set of steps to sort in some order
        Tree Traversal
        Graph Traversal
        Arrays

# ARRAYS ALGORITHMS
    - Kadane's Algorithm
    - Floyd's Cycle Detection Algorithm
    - KMP Algorithm
    - Quick Select Algorithm
    - Boyer-More Majority Vote Algorithm
    

# SORTING ALGORITHMS
    In sort algorithms, idea is to arrange the items of a list in a specific order.
    - Insertion Sort
    - Selection Sort
    - Merge Sort
    - Quick Sort
    - Bucket Sort
    - Heap Sort
    - Counting Sort

# SEARCHING ALGORITHMS
    Find a element in a data set. There are 2 types of search algorithms
    - Linear Search
    - Binary Search           # Method: Divide and Conquer
                for Linear Data Structures
----------------------------
def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

index = BinarySearch([1,2,3,4,5,6,7,8,9,10], 7)
print(index)

----------------------------
    - Depth First Search
                for Graph Data Structures
    - Breath First Search
                for Graph Data Structures

# GRAPH ALGORITHMS
    - Kruskal's Algorithm
    - Dijkstra's Algorithm
    - Bellman Ford Algorithm
    - Floyd Warshall Algorithm
    - Topological Sort Algorithm
    - Flood Fill Algorithm
    - Lee Algorithm
    
    
# HASHING ALGORITHMS
    Hashing lookup is currently the most widely used technique to find appropriate data by key or ID. We access data by its index.

# DYNAMIC PROGRAMMING ALGORITHMS
    DP is a method for solving a complex problem by breaking it down into simpler subproblems

# DIVIDE and CONQUER METHODOLOGY
    A divide-and-conquer algorithm recursively breaks down a problem into two or more sub-problems of the related type, until these become simple enough to be solved directly

# GREEDY ALGORITHMS
    We find a locally optimum solution and hope to find the optimal solution at the global level.

# BASIC ALGORITHMS
    - Huffman Coding Compression Algorithm
    - Euclid's Algorithm
    - Union Find Algorithm


