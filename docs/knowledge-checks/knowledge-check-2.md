# Knowledge Check 2

1. Questions
2. Lists
3. Tuples
4. Dictionaries / Hash Tables
5. Sets / Frozensets
6. Type Checking / Duck Typing
7. Shallow Copy vs Deep Copy

## Questions

### 1. True/False: Lists in Python are mutable.
**Answer**: True

### 2. Fill in the blank: To add an element to the end of a list, use the ________ method.
**Answer**: `append`

### 3. Select one: Which of the following is not a valid way to create an empty list?
- a) `[]`
- b) `list()`
- c) `{}`
- d) `[::]`

**Answer**: c

### 4. Select all that apply: Which of the following operations are valid for lists?
- a) Concatenation (`+`)
- b) Repetition (`*`)
- c) Indexing
- d) Slicing

**Answer**: a, b, c, d

### 5. True/False: Tuples in Python are immutable.
**Answer**: True

### 6. Fill in the blank: To create a tuple with a single element, you need to include a ________ after the element.
**Answer**: `comma`

### 7. Select one: Which of the following is a valid way to create an empty tuple?
- a) `()`
- b) `tuple()`
- c) Both a and b
- d) Neither a nor b

**Answer**: c

### 8. Select all that apply: Which of the following are advantages of using tuples over lists?
- a) Faster access and iteration
- b) Immutability
- c) Can be used as dictionary keys
- d) More memory efficient

**Answer**: a, b, c, d

### 9. True/False: Dictionaries in Python are ordered as of Python 3.7+.
**Answer**: True

### 10. Fill in the blank: To get a list of all keys in a dictionary, use the ________ method.
**Answer**: `keys`

### 11. Select one: Which of the following is not a valid way to create an empty dictionary?
- a) `{}`
- b) `dict()`
- c) `[]`
- d) `{()}`

**Answer**: c

### 12. Select all that apply: Which of the following can be used as dictionary keys?
- a) Integers
- b) Strings
- c) Tuples
- d) Lists

**Answer**: a, b, c

### 13. True/False: Hash tables in Python are implemented using dictionaries.
**Answer**: True

### 14. Fill in the blank: The average time complexity for dictionary operations (insert, delete, lookup) is ________.
**Answer**: `O(1)`

### 15. Select one: What is the main purpose of a hash function in a hash table?
- a) To encrypt data
- b) To compress data
- c) To map keys to array indices
- d) To sort data

**Answer**: c

### 16. Select all that apply: Which of the following are characteristics of a good hash function?
- a) Deterministic
- b) Fast to compute
- c) Minimizes collisions
- d) Produces reversible output

**Answer**: a, b, c

### 17. True/False: Lists in Python can contain elements of different data types.
**Answer**: True

### 18. Fill in the blank: To remove and return the last element from a list, use the ________ method.
**Answer**: `pop`

### 19. Select one: What is the time complexity of accessing an element in a list by index?
- a) `O(1)`
- b) `O(n)`
- c) `O(log n)`
- d) `O(n^2)`

**Answer**: a

### 20. Select all that apply: Which of the following methods modify a list in-place?
- a) `sort()`
- b) `reverse()`
- c) `append()`
- d) `extend()`

**Answer**: a, b, c, d

### 21. True/False: Tuples can be used as keys in a dictionary.
**Answer**: True

### 22. Fill in the blank: To convert a list to a tuple, use the ________ function.
**Answer**: `tuple`

### 23. Select one: What is the result of `(1, 2, 3) + (4, 5, 6)`?
- a) `(1, 2, 3, 4, 5, 6)`
- b) `((1, 2, 3), (4, 5, 6))`
- c) `[1, 2, 3, 4, 5, 6]`
- d) Error

**Answer**: a

### 24. Select all that apply: Which of the following are true about tuples?
- a) They are immutable
- b) They can be nested
- c) They support indexing
- d) They can be used in set operations

**Answer**: a, b, c, d

### 25. True/False: Dictionary keys must be immutable.
**Answer**: True

### 26. Fill in the blank: To safely get a value from a dictionary with a default if the key doesn’t exist, use the ________ method.
**Answer**: `get`

### 27. Select one: What happens if you try to access a key that doesn’t exist in a dictionary using square bracket notation?
- a) It returns None
- b) It raises a KeyError
- c) It returns an empty string
- d) It creates a new key-value pair

**Answer**: b

### 28. Select all that apply: Which of the following are methods to iterate over a dictionary?
- a) `items()`
- b) `keys()`
- c) `values()`
- d) `elements()`

**Answer**: a, b, c

### 29. True/False: Sets in Python can contain duplicate elements.
**Answer**: False

### 30. Fill in the blank: To create an empty set in Python, use the syntax _______().
**Answer**: `set`

### 31. Select one: Which of the following is not a valid way to create a set?
- a) `{1, 2, 3}`
- b) `set([1, 2, 3])`
- c) `set((1, 2, 3))`
- d) `{1: 'one', 2: 'two'}`

**Answer**: d

### 32. Select all that apply: Which of the following operations are supported by sets?
- a) Union
- b) Intersection
- c) Difference
- d) Symmetric difference

**Answer**: a, b, c, d

### 33. True/False: Frozen sets in Python are mutable.
**Answer**: False

### 34. Fill in the blank: To create a frozen set, use the ________ function.
**Answer**: `frozenset`

### 35. Select one: Which of the following methods is not available for frozen sets?
- a) `intersection()`
- b) `union()`
- c) `add()`
- d) `issubset()`

**Answer**: c

### 36. Select all that apply: What are the advantages of using frozen sets?
- a) They can be used as dictionary keys
- b) They are hashable
- c) They can be modified after creation
- d) They can be elements of other sets

**Answer**: a, b, d

### 37. True/False: The `type()` function returns a string representation of an object’s type.
**Answer**: False

### 38. Fill in the blank: To check if an object is an instance of a specific class or its subclasses, you use the __________ function.
**Answer**: `isinstance()`

### 39. Select one: Which of the following is the correct way to check if a variable `x` is of type `int`?
- a) `type(x) == int`
- b) `type(x) == 'int'`
- c) `isinstance(x, int)`
- d) `isinstance(x, 'int')`

**Answer**: c

### 40. Select all that apply: Which of the following statements about `isinstance()` are true?
- a) It can check for multiple types at once
- b) It considers inheritance
- c) It’s generally preferred over `type()` for type checking
- d) It can only check for built-in types

**Answer**: a, b, c

### 41. True/False: Shallow copy creates a new object, but references to nested objects are copied.
**Answer**: True

### 42. Fill in the blank: To perform a deep copy of an object, you need to import the ______ module.
**Answer**: `copy`

### 43. Select one: Which of the following methods creates a shallow copy of a list?
- a) `list.copy()`
- b) `list.deepcopy()`
- c) `copy.copy(list)`
- d) Both a and c

**Answer**: d

### 44. Select all that apply: When is a shallow copy sufficient?
- a) When dealing with immutable objects
- b) When the object contains only primitive types
- c) When you need to modify nested mutable objects independently
- d) When you want to create a new reference to the same object

**Answer**: a, b

### 45. True/False: Sets in Python are ordered collections.
**Answer**: False

### 46. Fill in the blank: The ________ method removes and returns an arbitrary element from a set.
**Answer**: `pop`

### 47. Select one: Which of the following set operations returns a new set with elements in either the first or second set, but not both?
- a) `union`
- b) `intersection`
- c) `difference`
- d) `symmetric_difference`

**Answer**: d

### 48. Select all that apply: Which of the following are true about frozen sets?
- a) They can be used as dictionary keys
- b) They support the `add()` method
- c) They can contain mutable objects
- d) They are hashable

**Answer**: a, d

### 49. True/False: The `type()` function can be used to check if an object is an instance of a custom class.
**Answer**: True

### 50. Fill in the blank: The expression `type(5)` returns ________.
**Answer**: `<class ‘int’>`

### 51. Select one: Which of the following is true about `isinstance()`?
- a) It can only check for a single type at a time
- b) It returns a string describing the object’s type
- c) It can check if an object is an instance of any class in a tuple of classes
- d) It’s slower than using `type()` for type checking

**Answer**: c

### 52. Select all that apply: When might you prefer `type()` over `isinstance()`?
- a) When you need to get the exact type of an object
- b) When you want to ignore inheritance
- c) When checking for multiple possible types
- d) When working with custom classes

**Answer**: a, b

### 53. True/False: Deep copy creates a new object and recursively copies all nested objects.
**Answer**: True

### 54. Fill in the blank: To perform a deep copy of an object `obj`, you would use `copy._________(obj)`.
**Answer**: `deepcopy`

### 55. Select one: Which of the following is not a valid way to create a shallow copy?
- a) `list[:]`
- b) `list.copy()`
- c) `copy.copy(list)`
- d) `copy.deepcopy(list)`

**Answer**: d

### 56. Select all that apply: When is a deep copy necessary?
- a) When working with nested mutable objects
- b) When you need to modify nested objects independently
- c) When dealing only with immutable objects
- d) When you want to ensure complete independence of the new object

**Answer**: a, b, d

### 57. True/False: Frozen sets can be elements of other sets.
**Answer**: True

### 58. Fill in the blank: The ________ method returns `True` if the set has no elements in common with other set(s).
**Answer**: `isdisjoint`
