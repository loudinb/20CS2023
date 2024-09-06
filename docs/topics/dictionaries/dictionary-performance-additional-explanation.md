# Dictionary Performance: Additional Explanation

In today's discussion on Python dictionaries, we discussed that they are fast thanks to their use of hash tables. The key idea is that finding the index of an element in an array is much quicker than searching for a value (like in a tree). This is what makes dictionaries so efficient, but it comes with some memory overhead. They need extra memory for their internal structure, and when a dictionary reaches capacity, it has to expand and sometimes reallocate memory to keep things organized.

At a low level, the speed of a dictionary comes from direct memory access. **Knowing the base address of an internal array allows you to calculate the position of any item by adding its index to the base address**. This avoids the need for a search and provides instant access to the data. In contrast, Python lists rely on indexing as well, but the key difference is that lists store elements sequentially. So, if you want to access an item by its index, it’s also quick. However, when you search for an item by value, the list must scan each element, leading to slower performance compared to a dictionary's hash lookup.

## Lists vs. Dictionaries

Python lists don’t have the overhead of maintaining a hash table, which keeps them simpler in structure and more memory-efficient for small collections.  When accessing an element by index in a list, Python can quickly compute the exact memory location of the item, making it just as fast as accessing a value in a dictionary by its key. This is because both operations rely on direct memory access—whether it's the index in a list or the hashed key in a dictionary. However, when you need to search for a specific value in a list, Python has to check each item sequentially until it finds a match, leading to slower performance as the list grows. This linear search takes O(n) time, meaning the longer the list, the longer it takes to find an item. In contrast, a dictionary can retrieve a value directly using its key, thanks to hashing, keeping the lookup time constant at O(1) regardless of the dictionary’s size. This makes dictionaries much more efficient for lookups based on unique keys compared to searching for values in a list.

## Example: Performance Comparison

Here's a simple example to illustrate the difference in performance between dictionaries and lists, focusing on the time it takes to search for a value in a list versus accessing an item by key in a dictionary.  On my machine, the dictionary access was **~250,000x** faster than searching for an element in a list.  As expected, accessing a list element by index took approximately the same time.

```python
# Create a large list and dictionary for comparison
large_list = [f"key_{i}" for i in range(1000000)]  # List with 1 million string elements
large_dict = {f"key_{i}": i for i in range(1000000)}  # Dictionary with 1 million string keys and integer values

# Accessing the 500,000th element by index in the list
time_list_index = %timeit -o large_list[500000]

# Searching for the string "key_500000" in the list
time_list_search = %timeit -o "key_500000" in large_list

# Accessing the value for key "key_500000" in the dictionary
time_dict_access = %timeit -o large_dict["key_500000"]

# Speedup for dictionary access over list search
speedup_search = int(time_list_search.average / time_dict_access.average)
print(speedup_search) # This will be a large number, indicating the speedup of dictionary access over list search.  On my machine, it was around 250,000.

# Speedup for dictionary access over list indexing
speedup_index = int(time_dict_access.average / time_list_index.average)
print(speedup_index)  # This will be 1, as both operations are O(1)
```

```{warning}
This example is dependent on having iPython installed or using a Jupyter Notebook as we are using the %timeit magic.
```